from django.contrib import admin
from django.urls import path
from . import views
from .apps import AppInstagramConfig

app_name = AppInstagramConfig.name

urlpatterns = [
    #view.main - function that make Pesentation of mapping base url (root in our case)
    #name="root" as in templates
    path("", views.main, name="root"),
    path("upload/", views.upload, name="upload"),
    path("pictures/", views.pictures, name="pictures"),

    path("pictures/edit/<int:pic_id>", views.edit, name="edit"),
    path("pictures/remove/<int:pic_id>", views.remove, name="remove"),    
]
