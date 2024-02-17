from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from .factories import ProductFactory
from django.contrib.auth.models import User

class ProductsTests(TestCase):
    
    
    def test_products_list(self):
        client = Client()
        product = ProductFactory()
        
        response = client.get(reverse('templates:product_list'))
        self.assertContains(response, product.id)
        self.assertContains(response, product.name)
           

    def test_edit_product_without_login(self):
        client = Client()
        product = ProductFactory()
        
        response = client.get(reverse('templates:update_product', args=[product.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_product_without_login(self):
        client = Client()
        product = ProductFactory()
        
        response = client.get(reverse('templates:delete_product', args=[product.id]))
        self.assertEqual(response.status_code, 302)
        
    def test_edit_product_as_admin(self):
        super_user = User.objects.create_superuser('superusertest')
        product = ProductFactory()
        client = Client()
        client.force_login(super_user, backend=None)
        
        response = client.get(reverse('templates:update_product', args=[product.id]))
        self.assertContains(response, product.id)
        self.assertContains(response, product.name)
        

    def test_delete_product_as_admin(self):
        super_user = User.objects.create_superuser('superusertest')
        product = ProductFactory()
        client = Client()
        client.force_login(super_user, backend=None)
        
        response = client.get(reverse('templates:delete_product', args=[product.id]))
        self.assertEqual(response.status_code, 200)