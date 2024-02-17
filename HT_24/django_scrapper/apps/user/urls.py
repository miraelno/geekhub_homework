from django.urls import path
from apps.user.views import logout_view
from apps.user.views import login_view

app_name = 'user'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
