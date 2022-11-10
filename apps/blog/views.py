import requests

from apps.dashboard.models import Post
from django.shortcuts import render

# Create your views here.

def main_page(request):
    posts = Post.objects.all()

    context = {'data': posts}
    return render(request, "apps/blog/home.html", context)


def single_post(request, slug):
    post = Post.objects.filter(slug=slug).first()

    context = {'post': post}
    return render(request, 'apps/blog/single-post.html', context)
