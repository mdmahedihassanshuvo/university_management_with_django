# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from .models import Faculty
from .serializer import FacultySerializer


class FacultyViewSet(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        if not email:
            return Response(
                {'details': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(
            user_name=data.get('email'),
            password=data.get('password'),
            role=data.get('role'),
        )

        faculty = Faculty.objects.filter(email=email).first()
        if faculty:
            return Response(
                {'details': 'Faculty already exist!'},
                status=status.HTTP_208_ALREADY_REPORTED
            )

        request.data['user'] = user.id
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
