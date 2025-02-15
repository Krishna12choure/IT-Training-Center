from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from customadmin.models import *

def home(request):
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    courses = Course.objects.order_by('-created_at')[:4]  # Fetch the latest 4 courses

    # Process each testimonial
    for testimonial in testimonials:
        rating = float(testimonial.rating)  # Convert to float
        testimonial.full_stars = int(rating)  # Get integer part
        testimonial.half_star = (rating - testimonial.full_stars) >= 0.5  # Check for half-star
        testimonial.empty_stars = 5 - (testimonial.full_stars + (1 if testimonial.half_star else 0))

    return render(request, 'main/home.html', {'testimonials': testimonials, 'courses': courses})

def about(request):
    return render(request, 'main/about.html')

def courses(request):
    # Fetch all courses from the database
    courses = Course.objects.all()
    
    # Pass courses to the template
    return render(request, 'main/courses.html', {'courses': courses})


def course_details(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'main/course_detail.html', {'course': course})

def placement(request):
    # Fetch all placements from the database
    placements = Placement.objects.all()
    
    # Pass placements to the template
    return render(request, 'main/placement.html', {'placements': placements})

def gallery(request):
    images = GalleryImage.objects.all()  # Fetch all gallery images
    return render(request, 'main/gallery.html', {'images': images})

def career(request):
    # Fetch all the job opportunities from the database
    job_opportunities = JobOpportunity.objects.all()
    
    # Pass the job opportunities to the template context
    return render(request, 'main/career.html', {'job_opportunities': job_opportunities})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            mobile_number=mobile_number,
            email=email,
            message=message,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # Redirect back to the contact page

    return render(request, "main/contact.html")

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save data to the database
            JobApplication.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                resume=form.cleaned_data['resume'],
            )
            messages.success(request, 'Your job application is submitted successfully.')
            return redirect('job_application')
    else:
        form = JobApplicationForm()

    return render(request, 'main/job_application.html', {'form': form})

def testimonial_page(request):
    testimonials = Testimonial.objects.all()
    
    # Process each testimonial
    for testimonial in testimonials:
        rating = float(testimonial.rating)  # Convert to float
        testimonial.full_stars = int(rating)  # Get integer part
        testimonial.half_star = (rating - testimonial.full_stars) >= 0.5  # Check for half-star
        testimonial.empty_stars = 5 - (testimonial.full_stars + (1 if testimonial.half_star else 0))  # Calculate empty stars

    return render(request, 'main/testimonial.html', {'testimonials': testimonials})