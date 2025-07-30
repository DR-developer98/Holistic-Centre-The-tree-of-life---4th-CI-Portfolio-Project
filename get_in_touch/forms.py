from .models import Enquiry
from django import forms


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'subject', 'email', 'message')
