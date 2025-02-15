from django.urls import path
from .views import *

urlpatterns = [
    path("login/", customadmin_login, name="customadmin_login"),
    path("logout/", customadmin_logout, name="customadmin_logout"),
    path("dashboard/", customadmin_dashboard, name="customadmin_dashboard"),
    
    path('courses/', courses_list, name='course_list'),
    path('courses/add/', add_course, name='add_course'),
    path('courses/edit/<int:course_id>/', edit_course, name='edit_course'),
    path('courses/delete/<int:course_id>/', delete_course, name='delete_course'),
    
    path('placements/', placement_list, name='placement_list'),
    path('placements/add/', add_placement, name='add_placement'),
    path('placements/edit/<int:id>/', edit_placement, name='edit_placement'),
    path('placements/delete/<int:id>/', delete_placement, name='delete_placement'),
    
    path('jobs_list/', job_list, name='job_list'),
    path('add/', add_job, name='add_job'),
    path('edit/<int:pk>/', edit_job, name='edit_job'),
    path('delete/<int:pk>/', delete_job, name='delete_job'),
    
    
    path('gallery/', gallery_list, name='gallery_list'),
    path('gallery/add/', gallery_add, name='gallery_add'),
    path('gallery/edit/<int:image_id>/', gallery_edit, name='gallery_edit'),
    path('gallery/delete/<int:image_id>/', gallery_delete, name='gallery_delete'),
    
    path("contacts/", contact_list, name="contact_list"),
    path("contacts/<int:contact_id>/", contact_detail, name="contact_detail"),
    path("contacts/<int:contact_id>/delete/", contact_delete, name="contact_delete"),
    
    path('admin/job-applications/', job_application_list, name='job_application_list'),
    path('admin/job-applications/<int:application_id>/', job_application_detail, name='job_application_detail'),
    path('admin/job-applications/<int:application_id>/delete/', job_application_delete, name='job_application_delete'),
    
    path('testimonials/', testimonial_list, name='testimonial_list'),
    path('testimonials/add/', add_testimonial, name='add_testimonial'),
    path('testimonials/view/<int:pk>/', view_testimonial, name='view_testimonial'),
    path('testimonials/delete/<int:pk>/', delete_testimonial, name='delete_testimonial'),
]