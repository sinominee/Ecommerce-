from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate #login, logout
from rest_framework.authtoken.models import Token

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


        messages.success(request, "You have been Logged in successfully")
        return redirect ('invalid')



