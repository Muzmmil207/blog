from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("<slug:slug>/", views.single_post, name="single_post"),
]
