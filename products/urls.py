from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('products/', views.index),
    path('products/<int:pk>/', views.description),
    path('products/new/', views.new),
    path('products/trending/', views.trending),
]
