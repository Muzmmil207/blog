from django.urls import path

from . import views

urlpatterns = [
    path("", views.SearchPost.as_view(), name="search"),
]
