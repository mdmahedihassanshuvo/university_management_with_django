# Generated by Django 5.1.3 on 2024-11-09 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_utils', '0003_alter_academicfaculty_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=6)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contact_no', models.CharField(max_length=20)),
                ('present_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('guardian', models.CharField(choices=[('father', 'FATHER'), ('mother', 'MOTHER'), ('other', 'OTHER')], max_length=6)),
                ('guardian_name', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='profile_image/student/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academic_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic_utils.academicsemester')),
            ],
        ),
    ]
