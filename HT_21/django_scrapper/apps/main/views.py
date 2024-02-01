from django.shortcuts import redirect


def index(request):
    return redirect('templates:product_list')
