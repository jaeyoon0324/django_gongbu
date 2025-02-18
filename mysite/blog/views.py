from django.shortcuts import render

# Create your views here.
from .models import Post
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})