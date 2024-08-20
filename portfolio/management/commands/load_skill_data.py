from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection
from portfolio.models import Skill


class Command(BaseCommand):
    help = 'Load initial data into the Skill table from a JSON file'

    def handle(self, *args, **kwargs):
        file_path = Path(settings.BASE_DIR, 'data', 'bootstrap_skill.json')
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                # delete existing rows
                Skill.objects.all().delete()
                if connection.vendor == 'sqlite':
                    sql = "DELETE FROM sqlite_sequence WHERE name = 'portfolio_skill'"
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                # use data from sql to populate table
                for skill in data:
                    Skill.objects.create(**skill)
                self.stdout.write(self.style.SUCCESS('Successfully loaded initial Skills'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
