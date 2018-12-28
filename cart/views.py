from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# this decorator allow only Post requests, since this view is going to change data
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# Finally, we need a view to display the cart and its items.
def cart_detail(request):
    cart = Cart(request)
    # Updating product quantities in the cart
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                    initial={'quantity': item['quantity'], 'update': True})
        # We create an instance of CartAddProductFrom for each item in the cart
        # to allow changing product quantities. We initialize the form with the
        # current item quantity and set the update field to True so that
        # when we submit the form to the cart_add view, the current quantity is
        # replaced with the new one.
    return render(request, 'cart/detail.html', {'cart': cart})


