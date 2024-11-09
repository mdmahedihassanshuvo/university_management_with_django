from django.contrib import admin

# FROM LOCAL IMPORTS
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'designation',
        'email',
        'academic_faculty'
    )
    search_fields = ('name', 'email', 'designation')
    ordering = ('id',)
