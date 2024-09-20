from django import forms
from django.utils.translation import gettext_lazy as _

from.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']   
        widgets = {
            'name': forms.TextInput(attrs={'name': 'name', 'id': 'name', 'placeholder': _("what's your name")}),
            'email': forms.EmailInput(attrs={'name': 'email', 'id': 'email', 'placeholder': _("your email")}),
            'message': forms.Textarea(attrs={'name': 'user_message', 'id': 'contact-message', 'placeholder': _("tell us about our project")}),
        }