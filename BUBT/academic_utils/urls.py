
from django.urls import path

# FROM LOCAL IMPORTS
from .views import AcademicFacultyApiView


urlpatterns = [
    path(
        'academic-faculties/',
        AcademicFacultyApiView.as_view(),
        name="academic_faculties"
    ),
]