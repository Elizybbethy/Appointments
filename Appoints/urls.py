from django.urls import path
from .views import CreateAppointmentView, UserAppointmentsView
from Appoints import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', CreateAppointmentView.as_view(), name='create_appointment'),
    path('user_appointments/', UserAppointmentsView.as_view(), name='user_appointments'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='spare/index.html'), name= 'logout'),
]