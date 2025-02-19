# Generated by Django 5.1.5 on 2025-02-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0005_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
