from django import forms
from .models import InsuranceDocument


class InsuranceDocumentForm(forms.ModelForm):
    class Meta:
        model = InsuranceDocument
        fields = ['title', 'document']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter document title'
            }),
            'document': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }