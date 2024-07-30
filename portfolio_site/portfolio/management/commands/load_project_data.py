from pathlib import Path
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date, parse_datetime
from django.db import connection

from portfolio.models import Project, Skill


class Command(BaseCommand):
    help = 'Load initial data into the Project table from a JSON file'

    def handle(self, *args, **kwargs):
        file_path = Path(settings.BASE_DIR, 'data', 'bootstrap_project.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # delete existing rows
                Project.objects.all().delete()
                if connection.vendor == 'sqlite':
                    sql = "DELETE FROM sqlite_sequence WHERE name = 'portfolio_project'"
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                for project_data in data:
                    skills_ids = project_data.pop('skills', [])
                    created_date = project_data.pop('created_date', None)
                    update_date = project_data.pop('update_date', None)

                    project, created = Project.objects.update_or_create(
                        name=project_data['name'],
                        defaults={
                            'description': project_data['description'],
                            'detailed_description': project_data['detailed_description'],
                            'start_date': parse_date(project_data['start_date']),
                            'end_date': parse_date(project_data['end_date']),
                            'live_site_url': project_data['live_site_url'],
                            'github_repo_url': project_data['github_repo_url'],
                            'image': project_data['image']
                        }
                    )

                    # If project was created, set the created_date and update_date manually
                    if created:
                        if created_date:
                            project.created_date = parse_datetime(created_date)
                        if update_date:
                            project.update_date = parse_datetime(update_date)
                        project.save()

                    # Clear existing skills and add the new ones
                    project.skills.clear()
                    for skill_id in skills_ids:
                        try:
                            skill = Skill.objects.get(id=skill_id)
                            project.skills.add(skill)
                        except Skill.DoesNotExist:
                            self.stdout.write(self.style.WARNING(f'Skill with id {skill_id} does not exist.'))

                    project.save()

                self.stdout.write(self.style.SUCCESS('Successfully bootstrapped the database with initial data.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))