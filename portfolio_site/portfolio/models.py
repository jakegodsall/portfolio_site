from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    svg_icon = models.FileField(upload_to='portfolio/svg_icons/', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_for_skills_section = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    detailed_description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    live_site_url = models.URLField(blank=True)
    github_repo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    skills = models.ManyToManyField(Skill, related_name='projects')

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
