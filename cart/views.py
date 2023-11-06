from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Order, OrderItem


# Create your views here.
# def index(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})

def cart_summary(request):
    order_item = OrderItem.objects.all()
    order = Order.objects.all()
    context = {
        'order_item': order_item,
        'order': order,
    }
    return render(request, 'cart_summary.html', context)


def cart_add(request):
    item = get_object_or_404(Product)
    order_item = OrderItem.objects.get_or_create(item=item)
    order_qs = Order.objects.filter()
    if order_item.exists():
        order = order_qs[0]
        if order.items.filter().exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create()
        order.items.add(order_item)
    return redirect("core:cart_summary")


def cart_delete(request):
    pass


def cart_update(request):
    pass