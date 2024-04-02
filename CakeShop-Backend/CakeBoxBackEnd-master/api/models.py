from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Occasion(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
class Cake(models.Model):
    name=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    occasion=models.ForeignKey(Occasion,on_delete=models.CASCADE)
    options=(
        ('round','round'),
        ('square','square'),
        ('heart','heart')
    )
    shape=models.CharField(max_length=200,choices=options,default='round')
    layerOptions=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    layers=models.CharField(max_length=200,choices=layerOptions,default='1')
    price=models.FloatField()
    image=models.ImageField(upload_to='images',blank=True,null=True)

    @property
    def reviews(self):
        return Review.objects.filter(cake=self)

    def __str__(self) -> str:
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    
    status=models.CharField(max_length=100,choices=options,default="in-cart")
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=300)
    matter=models.CharField(max_length=200)
    options=(
        ("order_placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("delivered","delivered")
    )
    
    status=models.CharField(max_length=100,choices=options,default="order_placed")
    
    

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    comment=models.TextField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) -> str:
        return self.comment
    
class CakeImages(models.Model):
    Cake=models.ForeignKey(Cake,on_delete=models.CASCADE,related_name='images')
    images=models.ImageField(upload_to='media/')



    


