from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from portfolio.models import Skill


class Command(BaseCommand):
    help = 'Load initial data into the Skill table from a JSON file'

    def handle(self, *args, **kwargs):
        file_path = Path(settings.BASE_DIR, 'data', 'bootstrap_skill.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
            for skill in data:
                Skill.objects.create(**skill)
            self.stdout.write(self.style.SUCCESS('Successfully loaded initial Skills'))