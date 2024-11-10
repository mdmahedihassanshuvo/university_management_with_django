from django.db import models
from academic_utils.models import AcademicSemester
from user.models import User


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER')
    ]
    GUARDIAN_CHOICES = [
        ('father', 'FATHER'),
        ('mother', 'MOTHER'),
        ('other', 'OTHER')
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    contact_no = models.CharField(max_length=20)
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    guardian = models.CharField(max_length=6, choices=GUARDIAN_CHOICES)
    guardian_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_image/student/')
    status = models.BooleanField(default=True)
    academic_semester = models.ForeignKey(
        AcademicSemester,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
