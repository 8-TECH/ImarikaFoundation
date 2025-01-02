from django import forms
from .models import Donation, Volunteer, Event


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'phone_number', 'interest_area']


class EventRegistrationForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.filter(event_type='upcoming'))
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
