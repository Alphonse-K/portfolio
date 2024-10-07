from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django import forms
from users.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from users.utils.send_email import send_activation_email


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Ce champ est obligatoire')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Ce email exists deja')
        return email


class CustomAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        print(user)
        if not user:
            raise ValidationError('Email ou mot passe incorrect')
        
        if not user.is_active:
            send_activation_email(user)
            raise ValidationError(
                'Votre compte n\'est actif,' 
                 ' Consulter votre mail pour l\'activation.')
        
        return self.cleaned_data
    

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Entrez votre email', max_length=255)


    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Pas d'utilisateur enregistre avec cet email")
        return email
