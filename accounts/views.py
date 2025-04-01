from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/index.html")


def signup_view(request: HttpRequest) -> HttpResponse:
    form: UserCreationForm[User]

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user: User = form.save()
            login(request, user)
            messages.success(request, "Account was sucessfully created")
            return redirect("accounts:index")
        else:
            messages.error(request, "Please fix the errors below")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    form: AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("accounts:index")
