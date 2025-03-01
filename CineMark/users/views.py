from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def faz_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect("")
    else: 
        form = AuthenticationForm()
        return render(request, "users/login.html",{"form": form})

def se_registra(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("login")
    else:
        UserCreationForm()
        return render(request, "users/registrar.html",{"form": form})
    

def faz_logout(request):
    logout(request)
    return redirect("login")

