from django.db import models
import  datetime

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/images/')
    duration = models.CharField(max_length=100, default="3 Months", help_text="Example: 3 Months, 6 Weeks")
    live_project = models.BooleanField(default=False, help_text="Does this course include a live project?")
    training_format = models.CharField(
        max_length=100,
        choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Hybrid', 'Hybrid')],
        default='Offline'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
class Placement(models.Model):
    student_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='placement/students/', blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.company_name} ({self.position})"
    
    
class JobOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    education = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title or "Untitled"
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class Testimonial(models.Model):
    student_name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_name