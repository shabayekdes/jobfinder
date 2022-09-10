from django.db import models


# Create your models here.
from companies.models import Company


class Job(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title