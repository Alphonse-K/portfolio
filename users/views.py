from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from users.forms import CustomAuthenticationForm, CustomUserCreationForm, PasswordResetForm
from users.utils.send_email import send_activation_email
from django.utils.http import urlsafe_base64_decode
from django.db import transaction
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from users.models import User




class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class CustomSignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_email(user)
        messages.success(
            self.request,
            ("Votre compte a ete active, Veuillez consulter"
             "pour l'activer")
        )
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class UserActivationView(View):
    login_url = reverse_lazy('login')

    def get(self, request, uid, token):
        id = urlsafe_base64_decode(uid)
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return render(request, 'registration/activation_invalid.html')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                self.request,
                ("Votre compte est actif, connectez-vous!")
            )
            return redirect(self.login_url)
        return render(request, 'registration/activation_invalid.html')
    

class CustomLogoutView(View):
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        messages.success(
            self.request,
            ("Compte deconnecte")
        )
        return redirect(self.login_url)
    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            ("Consultez votre compte pour changer de mot passe.")
        )
        return response
    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            ("Mot de passe reinitialise avec succes")
        )
        return response
    

