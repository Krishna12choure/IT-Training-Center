# Generated by Django 5.1.5 on 2025-02-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0008_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='3 Months', help_text='Example: 3 Months, 6 Weeks', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='live_project',
            field=models.BooleanField(default=False, help_text='Does this course include a live project?'),
        ),
        migrations.AddField(
            model_name='course',
            name='training_format',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Hybrid', 'Hybrid')], default='Offline', max_length=100),
        ),
    ]
