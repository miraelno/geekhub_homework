from collections import defaultdict


def get_or_create_session_cart(request):
    return request.session.get("shopping_cart", defaultdict(dict))
