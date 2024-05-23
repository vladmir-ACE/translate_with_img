from django import forms
from .models import Translate

class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translate
        fields = ['image', 'french_text', 'english_text']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'french_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'english_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
