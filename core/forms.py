from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    """
    This form is for handling the data for the Contact model explicitly
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']