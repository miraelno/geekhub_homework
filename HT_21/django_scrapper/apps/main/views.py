from django.shortcuts import redirect, render


def index(request):
    return redirect('templates:product_list')
