from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
# Create your views here.

def login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                username = register_form.cleaned_data.get("username")
                password = register_form.cleaned_data.get("password1")
                register_form.save()
                new_user = authenticate(username=username,password =password)
                if new_user is not None:
                    login(request,new_user)
                    #redirect("home")
    else:
        pass
        #redirect("home")       
    register_form = SignUpForm
    context = {
        "register_form" : register_form
    }

    return render(request ,'role_app/login.html' , context)