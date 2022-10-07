from django.urls import path

from .views import (
    show_job,
    JobListView
)

app_name = 'jobs'

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("<int:id>/", show_job, name="detail"),
]
