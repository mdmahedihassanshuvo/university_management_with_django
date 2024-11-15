from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# FROM LOCAL IMPORTS
from .models import (
    AcademicFaculty
)
from .serializer import AcademicSerializer


class AcademicFacultyApiView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = AcademicFaculty.objects.all()
        serializer = AcademicSerializer(queryset, many=True)

        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
