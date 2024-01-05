from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics

from store.serializers import UserSerializer

from django.contrib.auth.models import User

class SignUpView(generics.ListCreateAPIView):

    serializer_class=UserSerializer
    queryset=User.objects.all()




