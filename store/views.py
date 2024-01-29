from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import authentication,permissions
from rest_framework.decorators import action

from store.serializers import UserSerializer,ProductSerializer,BasketItemSerializer,BasketSerializer
from store.models import Product

from django.contrib.auth.models import User

class SignUpView(generics.ListCreateAPIView):

    serializer_class=UserSerializer
    queryset=User.objects.all()



class ProductsView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def list(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    def update(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    def destroy(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    # add_to_basket
    # http://127.0.0.1:8000/api/products/{id}/add_to_basket/
    # method:post
    @action(methods=["post"],detail=True)
    def add_to_basket(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product_object=Product.objects.get(id=id)
        basket_object=request.user.cart

        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(basket=basket_object,product=product_object)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class BasketView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=request.user.cart #cart related name used in models
        serializer=BasketSerializer(qs)
        return Response(data=serializer.data)

    

    
    
