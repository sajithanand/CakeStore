from django.contrib.auth.models import User

from api.models import Cake,Cart,Order,Review,CakeImages

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
    

        
        
class CakeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeImages
        fields = ['images']
        
class CakeSerializer(serializers.ModelSerializer):
    occasion=serializers.StringRelatedField()
    reviews=ReviewSerializer(read_only=True,many=True)
    images = CakeImagesSerializer(many=True, read_only=True)
    class Meta:
        model=Cake
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    cake=CakeSerializer(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    cake=CakeSerializer(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Order
        fields='__all__'


    


