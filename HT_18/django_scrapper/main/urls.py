from django.urls import path

from main.views import AllProductsList
from . import views


urlpatterns = [
    path('', view=AllProductsList.as_view()),
    path('add/', views.add_product, name='add_product'),
]