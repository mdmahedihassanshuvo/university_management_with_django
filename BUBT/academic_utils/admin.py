from django.contrib import admin
from .models import AcademicSemester, AcademicFaculty, AcademicProgram


@admin.site.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'code',
        'start_month',
        'end_month'
    )
    search_fields = ('name', 'year', 'code')
    list_filter = ('year', 'start_month', 'end_month')
    ordering = ('-created_at',)


@admin.site.register(AcademicFaculty)
class AcademicFacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.site.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'eke_name', 'academic_faculty'
    )
    search_fields = ('name', 'eke_name')
    list_filter = ('academic_faculty',)
    ordering = ('-created_at',)
