from django.urls import path, include
from . import views

app_name = "pleer"

urlpatterns = [
    path("", views.index, name="index"),
]
