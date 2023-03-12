from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm ,LoginForm
# Create your views here.

def login(request):
    #if request.user.is_anonymous:
    registerform = SignUpForm()
    loginform = LoginForm
    if request.method == "POST":
        if "login" in request.POST:
            loginform = LoginForm(data=request.POST)
            if loginform.is_valid():
                username = loginform.cleaned_data.get("username")
                password = loginform.cleaned_data.get("password")
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    print("not None")
                    auth_login(request, user)
                    messages.success(request, (f"Successfully Loged In {username}"))
                    # most of my users are in staff so i redirect to admin till create home page 
                    return redirect('/admin')
                else:
                    print("None")
                    messages.success(request, ("There Was An Error Logging In, Try Agin..."))
                    #return redirect('login')
        if "register" in request.POST:
            registerform = SignUpForm(request.POST, request.FILES)
            if registerform.is_valid():
                registerform.save()
    else:
        print("in else")
        loginform = LoginForm()
        registerform = SignUpForm()

       

    context = {
        "register_form" : registerform,
        "login_form"    : loginform
    }

    return render(request ,'role_app/login.html' , context)
