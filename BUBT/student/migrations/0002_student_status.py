# Generated by Django 5.1.3 on 2024-11-10 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
