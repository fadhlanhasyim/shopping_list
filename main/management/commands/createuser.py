from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Automatically creates a superuser in production'

    def handle(self, *args, **options):
        if not User.objects.filter(username='tes').exists():
            User.objects.create_superuser('tes', 'admin@example.com', 'tes')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
