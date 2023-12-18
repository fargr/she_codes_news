# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory, Category
from django.core.validators import EmailValidator

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory 
        fields = ['title', 'pub_date', 'content', 'preview', 'category', 'image']
        widgets = {          
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Write your preview: this will appear below your title" }),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(
                format='%m/%d/%Y %H:%M',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'datetime-local'
                }
            )
        }

# class ContactForm(forms.form):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(validators=[EmailValidator()})
#     message = forms.CharField(widget=forms.Textarea)

