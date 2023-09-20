from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Appointment(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_appointments', null=True, blank=True)
    title = models.CharField(max_length=200,null=False,blank=False)
    client_Name =models.CharField(max_length=50,null=False,blank=False)
    date = models.DateField()
    time = models.TimeField(null=False,blank=False)
    description = models.TextField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('user_appointments') 