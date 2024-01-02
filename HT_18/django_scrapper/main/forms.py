from django import forms


class ProductForm(forms.Form):
    product_ids = forms.CharField(max_length=100)
