from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import JobApplication
from .models import *
from .forms import PlacementForm,CourseForm,JobOpportunityForm,TestimonialForm

# Create your views here.
def customadmin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('customadmin_dashboard')  # Redirect to logged-in page
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password.")
            return render(request, 'customadmin/login.html')

    return render(request, 'customadmin/login.html')

def customadmin_logout(request):
    logout(request)
    return redirect('home')


@login_required
def customadmin_dashboard(request):
    # Get the total count for each model
    courses_count = Course.objects.count()
    placements_count = Placement.objects.count()
    job_opportunities_count = JobOpportunity.objects.count()
    gallery_images_count = GalleryImage.objects.count()
    contact_messages_count = ContactMessage.objects.count()
    testimonial_count = Testimonial.objects.count()
    

    # Pass the counts to the template
    context = {
        'courses_count': courses_count,
        'placements_count': placements_count,
        'job_opportunities_count': job_opportunities_count,
        'gallery_images_count': gallery_images_count,
        'contact_messages_count': contact_messages_count,
        'testimonial_count':testimonial_count,
    }

    return render(request, 'customadmin/dashboard.html', context)

@login_required
def courses_list(request):
    courses = Course.objects.all()  # Get all courses from the database
    return render(request, 'customadmin/courses/courses_list.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')  # Redirect to list of courses
        else:
            messages.error(request, "Error adding course. Please try again.")
    else:
        form = CourseForm()
    return render(request, 'customadmin/courses/add_course.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')  # Redirect to list of courses
        else:
            messages.error(request, "Error updating course. Please try again.")
    else:
        form = CourseForm(instance=course)
    return render(request, 'customadmin/courses/edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('course_list')  # Redirect to list of courses
    return render(request, 'customadmin/courses/delete_course.html', {'course': course})


# List all placements
@login_required
def placement_list(request):
    placements = Placement.objects.all()
    return render(request, 'customadmin/placement/placement_list.html', {'placements': placements})

# Add a new placement
@login_required
def add_placement(request):
    if request.method == 'POST':
        form = PlacementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Placement added successfully.")
            return redirect('placement_list')  # Ensure you have a URL for placement_list
    else:
        form = PlacementForm()
    
    return render(request, 'customadmin/placement/add_placement.html', {'form': form})

# Edit a placement
@login_required
def edit_placement(request, id):
    placement = get_object_or_404(Placement, id=id)
    if request.method == 'POST':
        form = PlacementForm(request.POST, request.FILES, instance=placement)
        if form.is_valid():
            form.save()
            messages.success(request, "Placement updated successfully.")
            return redirect('placement_list')
    else:
        form = PlacementForm(instance=placement)
    return render(request, 'customadmin/placement/edit.html', {'form': form, 'placement': placement})

# Delete a placement
@login_required
def delete_placement(request, id):
    placement = get_object_or_404(Placement, id=id)
    placement.delete()
    messages.success(request, "Placement deleted successfully.")
    return redirect('placement_list')


# List all job opportunities
@login_required
def job_list(request):
    jobs = JobOpportunity.objects.all()
    return render(request, 'customadmin/careers/job_list.html', {'jobs': jobs})

# Add a new job opportunity
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobOpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job opportunity added successfully.")
            return redirect('job_list')
    else:
        form = JobOpportunityForm()
    return render(request, 'customadmin/careers/add_job.html', {'form': form})

# Edit an existing job opportunity
@login_required
def edit_job(request, pk):
    job = get_object_or_404(JobOpportunity, pk=pk)
    if request.method == 'POST':
        form = JobOpportunityForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job opportunity updated successfully.")
            return redirect('job_list')
    else:
        form = JobOpportunityForm(instance=job)
    return render(request, 'customadmin/careers/edit_job.html', {'form': form, 'job': job})

# Delete a job opportunity
@login_required
def delete_job(request, pk):
    job = get_object_or_404(JobOpportunity, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job opportunity deleted successfully.")
        return redirect('job_list')
    return render(request, 'customadmin/careers/delete_job.html', {'job': job})

@login_required
def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'customadmin/gallery/gallery_list.html', {'images': images})

@login_required
def gallery_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        if image:
            GalleryImage.objects.create(title=title, image=image)
            messages.success(request, "Image added successfully!")
            return redirect('gallery_list')
        else:
            messages.error(request, "Please select an image to upload.")

    return render(request, 'customadmin/gallery/gallery_add.html')


@login_required
def gallery_edit(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            image.title = title
        
        if 'image' in request.FILES:
            image.image = request.FILES['image']
        
        image.save()
        messages.success(request, "Image updated successfully!")
        return redirect('gallery_list')

    return render(request, 'customadmin/gallery/gallery_edit.html', {'image': image})

@login_required
def gallery_delete(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)

    if request.method == 'POST':
        image.delete()
        messages.success(request, "Image deleted successfully!")
        return redirect('gallery_list')

    return render(request, 'customadmin/gallery/gallery_delete.html', {'image': image})

@login_required
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by('-created_at')  # Order by latest
    return render(request, "customadmin/contact/contact_list.html", {"contacts": contacts})

@login_required
def contact_detail(request, contact_id):
    contact = get_object_or_404(ContactMessage, id=contact_id)
    return render(request, "customadmin/contact/contact_detail.html", {"contact": contact})

@login_required
def contact_delete(request, contact_id):
    contact = get_object_or_404(ContactMessage, id=contact_id)
    contact.delete()
    messages.success(request, "Contact message deleted successfully.")
    return redirect("contact_list")

@login_required
def job_application_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'admin/job_application_list.html', {'applications': applications})

@login_required
def job_application_detail(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    return render(request, 'customadmin/applications/job_application_detail.html', {'application': application})

@login_required
def job_application_delete(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    application.delete()
    messages.success(request, "Job application deleted successfully.")
    return redirect('job_application_list')

# List Testimonials
@login_required
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'customadmin/testimonial/testimonial_list.html', {'testimonials': testimonials})

# Add Testimonial
@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial added successfully!")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'customadmin/testimonial/add_testimonial.html', {'form': form})

# View Testimonial Details
@login_required
def view_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    return render(request, 'customadmin/testimonial/view_testimonial.html', {'testimonial': testimonial})

#  Delete Testimonial
@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    messages.success(request, "Testimonial deleted successfully!")
    return redirect('testimonial_list')