from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR("No users found. Please create a user first."))
            return

        user = User.objects.first()
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i + 1}",
                description=f"Description for listing {i + 1}",
                location=random.choice(['Paris', 'New York', 'Tokyo', 'London']),
                price_per_night=random.randint(50, 500),
                owner=user
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
