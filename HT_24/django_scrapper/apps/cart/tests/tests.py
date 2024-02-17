from django.test import TestCase, Client
from django.urls import reverse
from apps.products.tests.factories import ProductFactory
from django.contrib.auth.models import User


class CartTestCases(TestCase):

    def test_add_to_cart_without_login(self):
        client = Client()
        product = ProductFactory()
        
        response = client.get(reverse('cart:cart_add', args=[product.id]))
        self.assertEqual(response.status_code, 302)
            
    def test_add_to_cart_as_logged_in_user(self):
        user = User.objects.create_superuser('superusertest')
        product = ProductFactory()
        client = Client()
        client.force_login(user, backend=None)
        
        client.get(reverse('cart:cart_add', args=[product.id]))
        response = client.get(reverse('templates:cart_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.id)
        
    def test_clear_cart(self):
        user = User.objects.create_superuser('superusertest')
        product = ProductFactory()
        client = Client()
        client.force_login(user, backend=None)
        
        client.get(reverse('cart:cart_clear'))
        response = client.get(reverse('templates:cart_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, product.id)
        