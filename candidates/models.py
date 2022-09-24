from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=Candidate)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CANDIDATE":
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_id = models.IntegerField(null=True, blank=True)
