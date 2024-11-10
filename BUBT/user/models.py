from django.db import models


class User(models.Model):
    password = models.CharField(max_length=20)
    needPasswordChange = models.BooleanField(default=True)
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role
