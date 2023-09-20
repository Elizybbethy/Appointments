from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['assigned_to','title', 'client_Name','date', 'time', 'description']
        
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))