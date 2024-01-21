from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_view, login_view


app_name = 'user'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]