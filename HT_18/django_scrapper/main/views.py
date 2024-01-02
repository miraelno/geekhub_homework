import logging

from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import ProductForm

from main.models import Product

logger = logging.getLogger('django')

class AllProductsList(ListView):
    model = Product
    paginate_by = 20
    template_name = 'product_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Products list"
        return context


def add_product(request):
    form = ProductForm(request.POST)
    
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "product_index.html", {'form': form})