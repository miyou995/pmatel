from decimal import Context
from .cart import Cart

def cart_context(resquest):
    cart= Cart(resquest)
    context = {
        'cart': cart,
        'cart_total_price': cart.get_total_price(),
        'cart_length' : cart.product_count(),
    }
    return context