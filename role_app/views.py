from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm ,LoginForm
# Create your views here.

def login(request):
    #if request.user.is_anonymous:
    if request.method == "POST":
        register_form = SignUpForm(request.POST, request.FILES)
        loginform = LoginForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            
            '''
            username = register_form.cleaned_data.get("username")
            password = register_form.cleaned_data.get("password1")
            new_user = authenticate(username=username,password =password)
            if new_user is not None:
                login(request,new_user)
                #redirect("home")'''
            
        elif loginform.is_valid():
            username = loginform.cleaned_data.get("username")
            password = loginform.cleaned_data.get("password1")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, ("Successfully Loged In {{username}}"))
                return redirect('admin')
            else:
                messages.success(request, ("There Was An Error Logging In, Try Agin..."))
                #return redirect('login')
    else:
        register_form = SignUpForm
        loginform = LoginForm 



    context = {
        "register_form" : register_form,
        "login_form"    : loginform
    }

    return render(request ,'role_app/login.html' , context)

'''
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        
'''