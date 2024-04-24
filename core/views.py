from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate #login, logout
from rest_framework.authtoken.models import Token
from .serializers import *

# from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib import messages
# Create your views here.
@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    # username = request.POST['username']
    # password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token,_= Token.objects.get_or_create(user=user)
        return Response({
            'user':user.get_username(),
            'token':token.key
        })
    # messages.success(request, "You have been Logged in successfully")
    return Response('invalid')


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    password = serializer.validated_data.get('password')
    # conform_password = serializer.validated_data.get('conform_password')
    user=User.objects.create_user(email=email, password=password)

    if user:
        return Response('user has been created')
    return Response("Something went wrong")

    # email=request.data.get('email')
    # settings.AUTH_USER_MODEL.objects.filter(email=email).exists()    
