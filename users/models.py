from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser',
        blank=True
    )

    def __str__(self):
        return self.username











