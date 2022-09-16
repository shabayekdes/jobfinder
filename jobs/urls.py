from django.urls import path

from .views import show_job

app_name = 'jobs'

urlpatterns = [
    path("<int:id>/", show_job, name="detail"),
]
