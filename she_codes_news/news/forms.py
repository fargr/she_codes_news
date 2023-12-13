# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.core.validators import EmailValidator


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory 
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }

# class ContactForm(forms.form):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(validators=[EmailValidator()})
#     message = forms.CharField(widget=forms.Textarea)

