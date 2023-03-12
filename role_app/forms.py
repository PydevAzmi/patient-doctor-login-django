from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .models import User
class SignUpForm(UserCreationForm):
    
    def __init__(self, *args , **kwargs ) :
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'type':"text" ,
            'id':"registerName",
            'class':"form-control",
        })
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'id':"registerUsername",
            'class':"form-control" ,
        })
        self.fields['email'].widget.attrs.update({
            'type':"email",
            'id':"registerEmail" ,
            'class':"form-control",
        })
        self.fields['password1'].widget.attrs.update({
            'type':"password",
            'id':"registerPassword" ,
            'class':"form-control" 
        })
        self.fields['password2'].widget.attrs.update({
            'type':"password",
            'id':"registerRepeatPassword",
            'class':"form-control",
        })
        self.fields['role'].widget.attrs.update({
            'required' : ''
        })
    
        
    class Meta:
        model = User
        fields= ['first_name', 'username', 'email', 'password1', 'password2','role']
        widgets={
            'role': forms.RadioSelect()
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
                'class'    : 'form-control',
                'required' : '',
                'type'     : "username",
                'id'       : "loginName",
                'class'    : "form-control"
            })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
                'class'    : 'form-control',
                'required' : '',
                'type'     :"password",
                'id'       :"loginPassword",
                'class'    :"form-control" })
    class Meta:
        model = User
        fields = ('username', 'password')