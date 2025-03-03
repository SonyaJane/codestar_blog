from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    
    
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**  post: An instance of :model:`blog.Post`.
    **Template:** :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # render puts together the template and the context dictionary and returns an HttpResponse object with that rendered text.
    # The context is a dictionary mapping template variable names to Python objects.
    # When rendering a template, Django replaces variables in the template with values from the context dictionary.
    return render(
        request, # everything we receive from the user via the Internet
        "blog/post_detail.html", # the template we want to render
        {"post": post, "coder": "Sonya"}, # things we want to pass to the template, in the form of a dictionary
    )
