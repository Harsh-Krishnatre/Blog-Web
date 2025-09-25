# dashboard/management/commands/create_missing_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import Profile  # Import your Profile model

class Command(BaseCommand):
    help = 'Creates missing user profiles'

    def handle(self, *args, **options):
        count = 0
        for user in User.objects.all():
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                count += 1
                self.stdout.write(f'Created profile for {user.username}')
        
        self.stdout.write(self.style.SUCCESS(f'Created {count} profiles'))