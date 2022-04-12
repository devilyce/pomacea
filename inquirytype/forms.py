from django import forms

from inquiryform.models import Inquiries


class CustomerForms(forms.ModelForm):
    class Meta:
        model = Inquiries
        fields = {
            'inquiry_type', 'first_name', 'last_name', 'middle_name', 'email', 'contact_number', 'mobile_number',
            'address',
        }

        widgets = {
            'inquiry_type': forms.Select(attrs={'class': 'form-select', 'name': 'inquiry_type'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'middle_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
            'contact_number': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'number', 'name': 'contact_number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'name': 'address', }),
        }
