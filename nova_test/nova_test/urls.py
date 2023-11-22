from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("google_drive_api.urls")),
]
