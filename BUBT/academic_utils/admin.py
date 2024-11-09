from django.contrib import admin
from .models import AcademicSemester, AcademicFaculty, AcademicProgram


@admin.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'year',
        'code'
    )
    list_filter = ('year',)
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(AcademicFaculty)
class AcademicFacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'eke_name', 'academic_faculty'
    )
    search_fields = ('name', 'eke_name')
    list_filter = ('academic_faculty',)
    ordering = ('id',)
