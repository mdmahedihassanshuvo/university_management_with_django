from rest_framework import serializers

# FROM LOCAL IMPORTS
from .models import (
    AcademicFaculty,
)


class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicFaculty
        fields = '__all__'
