# Generated by Django 3.2.9 on 2021-12-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_library'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skill',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='user_skills', to='skill.Skill'),
        ),
    ]