# Generated by Django 5.0.7 on 2024-07-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_skill_svg_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='svg_icon',
            field=models.FileField(blank=True, upload_to='svg_icons/'),
        ),
    ]