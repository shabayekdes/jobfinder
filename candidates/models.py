from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CANDIDATE = "CANDIDATE", "Candidate"
        COMPANY = "COMPANY", "Company"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class CandidateManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CANDIDATE)


class Candidate(User):
    base_role = User.Role.CANDIDATE

    accounts = CandidateManager()

    class Meta:
        proxy = True
