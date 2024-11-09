from django.db import models
from django.core.exceptions import ValidationError


class AcademicSemester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=1)
    start_month = models.DateField()
    end_month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'year')

    def clean(self):
        if self.start_month >= self.end_month:
            raise ValidationError("Start month must be before end month.")

    def __str__(self):
        return self.name


class AcademicFaculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AcademicProgram(models.Model):
    name = models.CharField(max_length=100)
    eke_name = models.CharField(max_length=10)
    academic_faculty = models.ForeignKey(
        AcademicFaculty,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
