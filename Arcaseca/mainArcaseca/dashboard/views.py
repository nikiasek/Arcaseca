from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.
def dashboard(request):
    return render(request, "index.html", {})

def login_user(request):
    if request.method == "POST":
        username1 = request.POST["username"]
        password1 = request.POST["password"]
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, ("logged in!"))
            return redirect("dashboard")
        else:   
            messages.success(request, ("Wrong credentials. Try again!"))
            return redirect("login")
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "succesfuly logged out!")
    return redirect("login")