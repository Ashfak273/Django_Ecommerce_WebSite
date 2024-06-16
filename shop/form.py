# 47
from django.contrib.auth.forms import UserCreationForm
from .models import User

# 50
from django import forms 

class CustomUserForm(UserCreationForm):
    # 50 overwrite fields before pass
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter User Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']