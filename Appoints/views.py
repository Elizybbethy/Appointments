from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Appointment
from .forms import AppointmentForm


class CreateAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'create_appointment.html'
    form_class = AppointmentForm
    success_url = '/user_appointments/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserAppointmentsView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'user_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(assigned_to=self.request.user)
    
