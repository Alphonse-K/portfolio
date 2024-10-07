from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from folioapp.models import MyProfile, ContactModel


class MyProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = '__all__'
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyProfile.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Ce email exists deja')
        return email
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'comment')

        error_messages = {
            'name': {
                'required': 'Fourniser un nom'
            },

            'email': {
                'required': 'J\' aurais besoin de cette email pour vous recontacter'
            },

            'comment': {
                'required': 'Donnez un apercu de ce que vous souhaitez'
            }

        }

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Entrer une addresse email valide')
        return email
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError("Le nom doit avoir 3 characteres minimum")
        return name
    
    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) < 10:
            raise ValidationError("Le message doit contenir 10 characters minimum")
        return comment
