# Generated by Django 5.0.1 on 2024-02-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
