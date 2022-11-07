from django.contrib import admin

from .models import Category, Post, PostComment, PostImage, PostMeta, PostTags


class PostImageInline(admin.TabularInline):
    model = PostImage


class PostMetaInline(admin.TabularInline):
    model = PostMeta


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "meta_title")
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title__startswith", )
    list_filter = ['is_published']
    inlines = [
        PostImageInline,
        PostMetaInline,
    ]

admin.site.register(Category)
admin.site.register(PostComment)
admin.site.register(PostTags)
