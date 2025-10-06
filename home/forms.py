from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["people","date","time","dietary_restriction"]