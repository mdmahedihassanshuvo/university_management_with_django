from django.contrib import admin

# FROM LOCAL IMPORTS
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'academic_semester'
    )
    search_fields = ('email',)
    ordering = ('id',)
