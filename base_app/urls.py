# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register_user'),
    path('verify/', verify_account, name='verify_account'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
