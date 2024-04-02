from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework import authentication,permissions

from api.serializers import UserSerializer,CakeSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from api.models import Cake,Cart,Order,Review,Occasion


# Create your views here.

class UsersView(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CakesView(viewsets.ModelViewSet):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Cake.objects.all()
        if "category" in self.request.query_params:
            cat = self.request.query_params.get("category")
            qs = qs.filter(occasion__name=cat)
        return qs.prefetch_related('images')



#   url:'http://127.0.0.1:8000/api/cakes/:id/add_to_cart/' 
    @action(methods=['POST'],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        serializer=CartSerializer(data=request.data)
        cake_obj=Cake.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(cake=cake_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
#   url:'http://127.0.0.1:8000/api/cakes/:id/place_order/' 
    @action(methods=['POST'],detail=True)
    def place_order(self,request,*args,**kwargs):
        serializer=OrderSerializer(data=request.data)
        cake_obj=Cake.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(cake=cake_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    

#   url:'http://127.0.0.1:8000/api/cakes/:id/add_review/' 
    @action(methods=['POST'],detail=True)    
    def add_review(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        cake_obj=Cake.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(cake=cake_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors) 
    
    @action(methods=["get"],detail=False)       
    def categories(self,request,*args,**kwargs):
        cats=Occasion.objects.values_list("name",flat=True)
        return Response(data=cats)       
            
    
class CartsView(viewsets.ModelViewSet):
    serializer_class=CartSerializer
    queryset=Cart.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    
    @action(detail=False, methods=['get'])
    def total_price(self, request):
        queryset = self.get_queryset()
        total_price = sum(cart.quantity * cart.cake.price for cart in queryset)
        return Response({'total_price': total_price})


    
    
class CartDeleteItem(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  
    
    @action(detail=True, methods=['delete'])
    def cart_delete(self,request,*args,**kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response( "Cart item deleted successfully")


    
class OrdersView(viewsets.ModelViewSet):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['delete'])
    def order_delete(self,request,*args,**kwargs):
        order_item = self.get_object()
        if order_item.user != request.user:
            return Response("You do not have permission to delete this cart item")
        
        order_item.delete()
        return Response( "Ordered item deleted successfully")
    

    

    


