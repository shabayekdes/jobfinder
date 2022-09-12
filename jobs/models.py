from django.db import models

# Create your models here.
from companies.models import Company
from categories.models import Category


class CareerLevelStatus(models.TextChoices):
    ENTRY_LEVEL = '1', 'Entry-level'
    INTERMEDIATE = '2', 'Intermediate'
    MID_LEVEL = '3', 'Mid-level'
    SENIOR = '4', 'Senior'
    MANAGE = '5', 'Manager'


class Job(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    career_level = models.CharField(max_length=1, choices=CareerLevelStatus.choices,
                                    default=CareerLevelStatus.ENTRY_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
