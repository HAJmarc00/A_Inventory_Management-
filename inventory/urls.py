from django.contrib import admin
from django.urls import path
from .views import index, SignUp

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
]
