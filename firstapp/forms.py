from django import forms
from .models import Product
from django.forms import ModelForm


class FormAddT(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'article', 'state', 'price', 'description']


class FormAdd(forms.Form):
    name = forms.CharField(max_length=13)
    article = forms.CharField(max_length=13)
    CHOICES = [('Закуплен', 'Закуплен'), ('На складе', 'На складе'), ('Выдан', 'Выдан')]
    state = forms.ChoiceField( choices=CHOICES)
    price = forms.IntegerField(min_value=0, max_value=100000)
    description = forms.CharField(widget=forms.Textarea)

