from django import forms
from .models import Enquiry

# Create your forms here


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'subject', 'email', 'message')
