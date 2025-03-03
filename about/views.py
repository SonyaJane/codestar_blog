from django.shortcuts import render
from .models import About

def about_me(request):
    """
    Renders the About page
    """
    # Get the latest about object
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
