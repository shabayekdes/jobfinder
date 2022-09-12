from django.urls import path

from .views import show_job

urlpatterns = [
    path("<int:id>/", show_job),
]