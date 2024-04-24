from django.urls import path
from .views import *


urlpatterns = [
    # path('login',views.login_user, name='login')
    path('login',login,name='login'),
    path('register',register,name='register'),
]