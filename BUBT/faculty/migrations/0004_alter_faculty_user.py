# Generated by Django 5.1.3 on 2024-11-10 02:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_faculty_user'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
