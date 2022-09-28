from django.urls import path

from .views import (
    show_profile
)

app_name = 'candidates'

urlpatterns = [
    path("profile/", show_profile, name="show_profile"),
]
