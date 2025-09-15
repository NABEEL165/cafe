from django import forms
from .models import *
from .models import contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['name', 'email', 'message']
from .models import TableBooking
class BookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        