import random
import datetime

from django.core.management import BaseCommand
from faker import Faker

from categories.models import Category
from companies.models import Company
from jobs.models import Job


class Command(BaseCommand):
    help = "Generate Fake Data"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(15):
            Category.objects.create(name=fake.name())
            Company.objects.create(name=fake.company())

        for _ in range(30):
            Job.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                category_id=random.randint(1, 15),
                company_id=random.randint(1, 15),
                type=random.randint(1, 4),
                gender=random.randint(1, 3),
                career_level=random.randint(1, 5),
                created_at=datetime.datetime.now()
            )
