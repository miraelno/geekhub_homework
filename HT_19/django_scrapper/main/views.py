from multiprocessing import Pool

from django.shortcuts import render
from .forms import ProductsAddForm

from django.views.generic import DetailView
from main.models import Product
from main.product_scrapper import save_scrapped_data


def product_list(request):
    return render(request, "product/product_list.html", {"products": Product.objects.all()})


def add_product(request):
    form = ProductsAddForm(request.POST)
    context = {"form": form}

    if form.is_valid():
        product_ids = form.cleaned_data.get("product_ids", "").split(" ")

        pool = Pool()
        try:
            pool.map(save_scrapped_data, product_ids)
        except Exception:
            context["started"] = False
            return render(request, "product/product_add.html", context)


        context["started"] = True
        context["product_ids"] = product_ids

    return render(request, "product/product_add.html", context)


class ProductDetail(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"

