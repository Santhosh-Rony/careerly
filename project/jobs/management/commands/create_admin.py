from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='jobPortal',
                email='chodipillisanthosh07@gmail.com',
                password='sanjay@123'
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created superuser: jobPortal')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Superuser already exists')
            ) 