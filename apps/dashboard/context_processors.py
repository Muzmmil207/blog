from .models import Category, PostTags


def categories(request):
    return {'categories': Category.objects.values("name", "slug")}


def tags(request):
    return {'tags': PostTags.objects.values("name", "slug")}
