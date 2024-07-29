from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from portfolio.models import Skill


class Command(BaseCommand):
    help = 'Load initial data into the Skill table from a JSON file'

    def handle(self, *args, **kwargs):
        # Check if the Product table is empty
        if Skill.objects.exists():
            self.stdout.write(self.style.WARNING('The Skill table is not empty. Skipping bootstrap.'))
            return

        file_path = Path(settings.BASE_DIR, 'data', 'bootstrap_skill.json')
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for skill in data:
                    Skill.objects.create(**skill)
                self.stdout.write(self.style.SUCCESS('Successfully loaded initial Skills'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
