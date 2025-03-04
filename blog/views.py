from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.contrib import messages

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')


    comment_form = CommentForm()
    
    # render puts together the template and the context dictionary and returns an HttpResponse object with that rendered text.
    # The context is a dictionary mapping template variable names to Python objects.
    # When rendering a template, Django replaces variables in the template with values from the context dictionary.
    return render(
        request, # everything we receive from the user via the Internet
        "blog/post_detail.html", # the template we want to render
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }, # things we want to pass to the template, in the form of a dictionary
    )
