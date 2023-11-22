from django.urls import path
from .views import create_file


urlpatterns = [
    path("create-file/", create_file, name="create-file"),
]
