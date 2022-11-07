from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.blog.urls')),
    # Third part app
    path("__debug__/", include("debug_toolbar.urls")),
]
