from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginUserForm


def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user and user.is_active:
                login(request, user)
                return redirect("main:product_list")
            else:
                messages.add_message(request, messages.ERROR, "No such user.")
    else:
        form = LoginUserForm()
    return render(request, "user/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main:product_list")
