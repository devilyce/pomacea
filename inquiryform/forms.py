from django import forms

from inquiryform.models import Inquiries, City


class InquiriesForm(forms.ModelForm):
    class Meta:
        model = Inquiries
        fields = {
            'inquiry_type', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'mobile_number',
            'address', 'state', 'city', 'zip_code',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'middle_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'name': 'phone_number'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'name': 'mobile_number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'name': 'address', }),
            'state': forms.Select(attrs={'class': 'form-select', 'name': 'state'}),
            'city': forms.Select(attrs={'class': 'form-select', 'name': 'city'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'name': 'zip_code'}),
            'inquiry_type': forms.Select(attrs={'class': 'form-select', 'name': 'inquiry_type'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city'].queryset = City.objects.none()

            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('state'))
                    self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
