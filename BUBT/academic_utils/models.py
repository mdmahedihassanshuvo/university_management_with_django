from django.db import models


class AcademicSemester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=1)
    start_month = models.DateField()
    end_month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    eke_name = models.CharField(max_length=5)
    academic_faculty = models.ForeignKey(
        AcademicFaculty,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
