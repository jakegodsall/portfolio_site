# Generated by Django 5.0.7 on 2024-09-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_skill_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='for_portfolio',
            field=models.BooleanField(default=False),
        ),
    ]
