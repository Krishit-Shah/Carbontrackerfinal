from django.core.management.base import BaseCommand
from footprint.utils import create_sample_tips
from footprint.models import SustainabilityTip


class Command(BaseCommand):
    help = 'Setup sample data for the Carbon Footprint Tracker'

    def handle(self, *args, **options):
        self.stdout.write('Setting up sample data...')
        
        # Create sample tips
        tips_data = create_sample_tips()
        created_count = 0
        
        for tip_data in tips_data:
            tip, created = SustainabilityTip.objects.get_or_create(
                title=tip_data['title'],
                defaults=tip_data
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created tip: {tip.title}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} sustainability tips!'
            )
        )
        
        # Set admin password
        from django.contrib.auth.models import User
        try:
            admin_user = User.objects.get(username='admin')
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('Admin password set to: admin123')
            )
        except User.DoesNotExist:
            self.stdout.write(
                self.style.WARNING('Admin user not found. Please create manually.')
            ) 