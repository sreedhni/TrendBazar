

from django.contrib.auth.models import User
from rest_framework import serializers

from store.models import Product,Basket,BasketItem

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","email","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product   
        fields="__all__" 




class BasketItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model=BasketItem
        fields="__all__"
        read_only_fields=["basket","product","created_at","updated_at"]

class BasketSerializer(serializers.ModelSerializer):
    owner=serializers.StringRelatedField()
    basket_item_count=serializers.CharField(read_only=True)
    
    class Meta:
        model=Basket
        fields="__all__"
    basket_items=BasketItemSerializer(many=True,read_only=True)

