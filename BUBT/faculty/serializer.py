from rest_framework import serializers

from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            'user'
            'name',
            'designation',
            'email',
            'contact_no',
            'gender',
            'date_of_birth',
            'present_address',
            'permanent_address',
            'profile_image',
            'academic_faculty',
        ]
