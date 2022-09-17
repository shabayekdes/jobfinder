from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.
from companies.models import Company
from categories.models import Category


class JobCareerLevels(models.IntegerChoices):
    ENTRY_LEVEL = 1, 'Entry-level'
    INTERMEDIATE = 2, 'Intermediate'
    MID_LEVEL = 3, 'Mid-level'
    SENIOR = 4, 'Senior'
    MANAGE = 5, 'Manager'


class JobTypes(models.IntegerChoices):
    FULL_TIME = 1, 'Full Time'
    PART_TIME = 2, 'Part Time'
    FREELANCE = 3, 'Freelance'
    TEMPORARY = 4, 'Temporary'


class JobGender(models.IntegerChoices):
    BOTH = 1, 'Both'
    MALE = 2, 'Male'
    FEMALE = 3, 'Female'


class JobQuerySet(models.QuerySet):
    def search(self, query=None):
        if query == "" or query is None:
            return self.none()
        lookup = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(company__name__icontains=query) |
                Q(category__name__icontains=query)
        )
        return self.filter(lookup)


class JobManager(models.Manager):
    def get_queryset(self):
        return JobQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Job(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    offered_salary = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/jobs', blank=True, default='media/jobs/default.png')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=JobTypes.choices, default=JobTypes.FULL_TIME)
    gender = models.CharField(max_length=1, choices=JobGender.choices, default=JobGender.BOTH)
    career_level = models.CharField(max_length=1, choices=JobCareerLevels.choices, default=JobCareerLevels.ENTRY_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = JobManager()

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title
