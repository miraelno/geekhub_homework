from django.shortcuts import render

from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from main.models import Product


class AllProductsList(ListView):
    model = Product
    paginate_by = 20
    template_name = 'product_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Products list"
        return context
