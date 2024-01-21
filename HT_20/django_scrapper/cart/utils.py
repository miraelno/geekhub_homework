def get_or_create_session_cart(request):
    return request.session.get("shopping_cart", [])

def get_product_from_cart(cart, product_id):
    for product in cart:
        if product.get(product_id):
            return product