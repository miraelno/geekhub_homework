def get_or_create_session_cart(request):
    cart = request.session.get('session_key')

    if 'session_key' not in request.session:
        cart = request.session['session_key'] = {}

    return cart