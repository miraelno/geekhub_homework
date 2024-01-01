from django.urls import path

from main.views import AllProductsList


urlpatterns = [
    path('', view=AllProductsList.as_view()),
]