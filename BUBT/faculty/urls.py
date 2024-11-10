from django.urls import path
from .views import FacultyViewSet

urlpatterns = [
    path(
        'faculty-create/',
        FacultyViewSet.as_view(),
        name='create_faculty'
    ),
]
