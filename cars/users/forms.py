from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,
                                                             'placeholder':"Введите имя",
                                                             }))
    
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'placeholder':"Введите пароль"}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        
        
class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username',
                  'phone', 
                  'email',
                  'password1',
                  'password2']
    
    
    # username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,
    #                                                          'placeholder':"Введите имя",
    #                                                          }))
    
    # phone = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder':"Введите Номер телефона BY"}),
    # )
    # email = forms.CharField(widget=forms.EmailInput(attrs={"autofocus": True,
    #                                                          'placeholder':"Введите email",
    #                                                          }))
    
    # password = forms.CharField(
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'placeholder':"Введите пароль"}),
    # )
    
    # password2 = forms.CharField(
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'placeholder':"Подтвердите пароль *"}),
    # )