from django.shortcuts import render
from django.contrib import messages # Import the messages framework
from .models import About
from .forms import CollaborateForm

def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST) # Populate the form instance with the POST data.
        if collaborate_form.is_valid():                       # Check if the form data is valid
            collaborate_form.save()                           # Save the form data to the database
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
            
    # Get the latest about object
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
        "about": about, 
         "collaborate_form": collaborate_form
         },
    )
