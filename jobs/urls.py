from django.urls import path

from .views import (
    show_job,
    list_job
)

app_name = 'jobs'

urlpatterns = [
    path("", list_job, name="list"),
    path("<int:id>/", show_job, name="detail"),
]
