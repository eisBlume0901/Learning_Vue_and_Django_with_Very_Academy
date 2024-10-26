
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView


urlpatterns = [
    path('posts/', PostView.as_view(), name='post'),
]