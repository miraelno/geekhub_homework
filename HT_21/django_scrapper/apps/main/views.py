from multiprocessing import Pool

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, DeleteView
from .mixins import AuthenticatedMixin
from apps.main.models import Product, Category
from apps.main.product_scrapper import save_scrapped_data

from .forms import ProductsAddForm
    
def product_list(request):
    category_id = request.GET.get('category_id')
    product_queryset = Product.objects.all()
    
    if category_id:
        product_queryset = product_queryset.filter(category_id=category_id)
        
    return render(
        request, "product/product_list.html", {"products": product_queryset, 'categories': Category.objects.all()}
    )


@login_required(login_url="/user/login/")
def add_product(request):
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, "You have no permissions for this action.")
        return redirect("main:product_list")

    form = ProductsAddForm(request.POST)
    context = {"form": form}

    if form.is_valid():
        product_ids = form.cleaned_data.get("product_ids", "").split(" ")

        pool = Pool()
        try:
            pool.map(save_scrapped_data, product_ids)
        except Exception as e:
            print(e)
            context["started"] = False
            return render(request, "product/product_add.html", context)

        context["started"] = True
        context["product_ids"] = product_ids

    return render(request, "product/product_add.html", context)


class ProductDetail(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"


class ProductEdit(AuthenticatedMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'brand', 'link', 'category']
    template_name = "product/product_edit.html"
    
    def get_success_url(self):
        return reverse('main:product_list')
    

class ProductDelete(AuthenticatedMixin ,DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    
    def get_success_url(self):
        return reverse('main:product_list')