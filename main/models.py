from django.db import models
import datetime

class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(default=datetime.datetime.now,blank=True)

    def __str__(self):
        return self.full_name