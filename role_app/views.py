from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
# Create your views here.

def login(request):
    #if request.user.is_anonymous:
    if request.method == "POST":
        register_form = SignUpForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            '''
            username = register_form.cleaned_data.get("username")
            password = register_form.cleaned_data.get("password1")
            new_user = authenticate(username=username,password =password)
            if new_user is not None:
                login(request,new_user)
                #redirect("home")'''
    else:
        register_form = SignUpForm
    context = {
        "register_form" : register_form
    }

    return render(request ,'role_app/login.html' , context)