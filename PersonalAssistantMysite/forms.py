from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact, Note


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Implement your phone number validation logic here
        # You can use regular expressions or other methods to validate the phone number
        if not phone_number.startswith('+'):
            raise ValidationError("Phone number must start with a '+' sign.")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Invalid email address.")
        return email


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
