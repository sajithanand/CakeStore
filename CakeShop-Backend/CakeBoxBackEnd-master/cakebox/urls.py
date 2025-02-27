"""
URL configuration for cakebox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf import settings
from django.conf.urls.static import static
from api import views
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()
router.register('api/register',views.UsersView,basename='users')
router.register('api/cakes',views.CakesView,basename='cakes')
router.register('api/carts',views.CartsView,basename='carts')
router.register('api/orders',views.OrdersView,basename='orders')
router.register('api/CartDel',views.CartDeleteItem,basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',ObtainAuthToken.as_view()),
    
]+router.urls+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
