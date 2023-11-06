from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'home.html')


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')


def trending(request):
    return HttpResponse('Trending Products')
