from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

from apps.cart.utils import get_or_create_session_cart
from apps.products.models import Product, Category
from apps.templates.forms import ProductsAddForm
from apps.templates.mixins import AuthenticatedMixin


@login_required(login_url="/user/login/")
def cart_list(request):
    cart = get_or_create_session_cart(request)
    return render(request, "cart/cart.html", context={"cart": cart})


def product_list(request):
    params = request.GET
    category_id = request.GET.get("category_id")
    product_queryset = Product.objects.all()

    if category_id:
        product_queryset = product_queryset.filter(category_id=category_id)

    return render(
        request,
        "product/product_list.html",
        {
            "products": product_queryset,
            "categories": Category.objects.all(),
            **params,
        },
    )


@login_required(login_url="/user/login/")
def add_product(request):
    if not request.user.is_superuser:
        messages.add_message(
            request, messages.ERROR, "You have no permissions for this action."
        )
        return redirect("templates:product_list")

    form = ProductsAddForm()
    context = {"form": form, **request.GET}

    return render(request, "product/product_add.html", context)


def product_detail(request, pk):
    return render(
        request,
        "product/product_detail.html",
        {"product": Product.objects.get(pk=pk)},
    )


class ProductEdit(AuthenticatedMixin, UpdateView):
    model = Product
    fields = ["name", "price", "description", "brand", "link", "category"]
    template_name = "product/product_edit.html"

    def get_success_url(self):
        return reverse("templates:product_list")


class ProductDelete(AuthenticatedMixin, DeleteView):
    model = Product
    template_name = "product/product_delete.html"

    def get_success_url(self):
        return reverse("templates:product_list")
