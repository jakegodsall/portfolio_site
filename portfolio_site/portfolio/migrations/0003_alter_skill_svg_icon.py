# Generated by Django 5.0.7 on 2024-07-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_skill_is_for_skills_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='svg_icon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
