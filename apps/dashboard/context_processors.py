from django.db.models import F, Value

from .models import Category, Post, PostTags


def categories(request):
    return {"categories": Category.objects.values("name", "slug")}


def tags(request):
    return {"tags": PostTags.objects.values("name", "slug")}


def posts_filters(request):
    posts = Post.published.all().only(
        "title", "category", "published_at","author"
    ).select_related(
        "author","category"
    ).values()

    return {
        "popular": posts.order_by("-reading_times")[:11],
        "trending": posts.order_by("-trending")[:11],
        "latest": posts.order_by("-published_at")[:11],
    }

