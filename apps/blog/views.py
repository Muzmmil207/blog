from apps.dashboard.models import Category, Post, PostComment
from django.db.models import Count
from django.shortcuts import redirect, render

# Create your views here.

def main_page(request):
    posts = Post.published.all()[:6].select_related("author")

    context = {"data": posts}
    return render(request, "apps/blog/home.html", context)


def single_post(request, slug):
    post = Post.objects.filter(slug=slug).annotate(
            comments_number=Count("postcomment")
        ).first()
    post.plus_one(request)

    if request.POST:
        PostComment.objects.create(
            post=post,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            comment=request.POST.get("comment"),
        )
        return redirect("single_post", slug=slug)

    comments = PostComment.objects.filter(post=post)

    context = {"post": post, "comments": comments}
    return render(request, "apps/blog/single-post.html", context)


def categories(request, slug):
    posts = Post.published.filter(category__name=slug)
    
    context = {"posts": posts}
    return render(request, "apps/blog/category.html", context)
