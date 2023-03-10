from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .models import User
class SignUpForm(UserCreationForm):
    bar = forms.ChoiceField( widget=forms.RadioSelect(), choices=[User.ROLES], required=True)
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