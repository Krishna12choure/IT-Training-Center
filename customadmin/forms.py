from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image', 'duration', 'live_project', 'training_format']
        
        widgets = {
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: 3 Months, 6 Weeks'}),
            'live_project': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'training_format': forms.Select(attrs={'class': 'form-select'}),
        }

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['student_name', 'company_name', 'position', 'image']
        
class JobOpportunityForm(forms.ModelForm):
    class Meta:
        model = JobOpportunity
        fields = ['title', 'description', 'location', 'experience', 'education']
        
        
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['student_name', 'testimonial_text', 'rating', 'image']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'testimonial_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5', 'step': '0.1'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }