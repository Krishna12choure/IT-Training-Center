from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('placement/', views.placement, name='placement'),
    path('gallery/', views.gallery, name='gallery'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('careers/application/', views.job_application, name='job_application'),
    path('Testimonial/', views.testimonial_page, name='Testimonial'),
    path('course-details/<int:id>/', views.course_details, name='course_details'),
    
]
