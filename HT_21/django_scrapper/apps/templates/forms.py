from django import forms


class ProductsAddForm(forms.Form):
    product_ids = forms.CharField(max_length=1000, required=True)


class ProductDetailForm(forms.Form):
    product_id = forms.CharField(max_length=100, required=True)
