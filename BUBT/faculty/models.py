from django.db import models

# FROM LOCAL IMPORTS
from academic_utils.models import AcademicFaculty


class Faculty(models.Model):
    GENDER_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER')
    ]
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contact_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_image/faculty/')
    academic_faculty = models.ForeignKey(
        AcademicFaculty,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
