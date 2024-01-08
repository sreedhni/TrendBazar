from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    picture=models.ImageField(upload_to="images",null=True)
    is_trending=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class Basket(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
  
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    @property
    def basket_items(self):
        qs=self.cartitem.all()
        return qs
    @property
    def basket_item_count(self):
        return self.cartitem.all().count()

class BasketItem(models.Model):
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cartitem") 
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)



def create_basket(sender,created,instance,**kwargs):
    if created:
        Basket.objects.create(owner=instance)



post_save.connect(create_basket,sender=User)



