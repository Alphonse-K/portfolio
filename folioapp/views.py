from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, FormMixin
from django.views import View
from folioapp.models import MyProfile, PorteFolio
from folioapp.forms import MyProfileForm, ContactForm
from blog.models import Post
from django.contrib import messages



class HomeView(View):
    template_name = 'folioapp/home.html'

    def get(self, request, *args, **kwargs):
        profile = MyProfile.objects.get(email='kamanalphonse@gmail.com')
        posts = Post.objects.all()[:3]
        context = {
            'portfolio': PorteFolio.objects.all()[:3],
            'profile': profile,
            'posts': posts
        }
        return render(request, self.template_name, context)


class MyProfileView(ListView):
    model = MyProfile
    template_name = 'folioapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_profile = MyProfile.objects.get(email='kamanalphonse@gmail.com')
        print(type(my_profile.first_name))
        context['my_profile'] = my_profile
        return context


class MyProfileUpdateView(UpdateView):
    model = MyProfile
    template_name = 'folioapp/profile_update.html'
    form_class = MyProfileForm
    success_url = reverse_lazy('folioapp:profile')


class ContactView(FormMixin, View):
    form_class = ContactForm
    success_url = reverse_lazy('folioapp:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Message envoyé"
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return redirect(self.success_url)


