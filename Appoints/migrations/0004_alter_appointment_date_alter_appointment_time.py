# Generated by Django 4.2.5 on 2023-09-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoints', '0003_appointment_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=0.0),
        ),
    ]
