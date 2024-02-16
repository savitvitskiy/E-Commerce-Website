from django.shortcuts import render, get_object_or_404
# from .models import Order, OrderItem
from .cart import Cart
from products.models import Product
from django.http import JsonResponse


# Create your views here.
# def index(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    return render(request, 'cart_summary.html')


def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))

        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to a session
        cart.add(product=product)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # Return a response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
