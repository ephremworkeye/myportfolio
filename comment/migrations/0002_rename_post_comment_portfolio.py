# Generated by Django 3.2.9 on 2021-12-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='portfolio',
        ),
    ]
