# Generated by Django 5.0.1 on 2024-03-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]