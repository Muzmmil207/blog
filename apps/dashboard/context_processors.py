from .models import Category, PostTags


def categories(request):
    return {'categories': Category.objects.values("name")}

