# Generated by Django 3.2.9 on 2021-12-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='model_design_url',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
