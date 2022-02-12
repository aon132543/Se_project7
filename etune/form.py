from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Scholar_news
        fields = '__all__'