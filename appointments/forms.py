from django import forms
from .models import Appointment
from accounts.models import User

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer', 'title', 'date', 'time', 'notes']

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        if company:
            self.fields['customer'].queryset = User.objects.filter(user_type='customer')
