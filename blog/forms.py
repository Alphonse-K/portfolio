from django import forms
from blog.models import Comment
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 5, 
                'cols': 8,
                'placeholder': 'Entrer votre commentaire...',
            })
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 1:
            raise ValidationError('Votre commentaire est trop court')
        return content