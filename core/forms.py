from django import forms
from .models import Feedback

class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'feedback']
        widgets = {
                'email':forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'example@gmail.com'}),
                'feedback':forms.Textarea(attrs={'class': 'form-control', 'id': 'floatingTextarea', 'placeholder': 'Leave a comment here...'})
                }