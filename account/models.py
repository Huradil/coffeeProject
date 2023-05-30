from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    USER_ROLE = 'user'
    ADMIN_ROLE = 'admin'

    ROLE_CHOICES = (
        (USER_ROLE, 'User'),
        (ADMIN_ROLE, 'Admin'),
    )

    phone_number=models.CharField(max_length=13)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default=USER_ROLE)
    groups = models.ManyToManyField(Group, related_name='users', blank=True)
    user_groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users', blank=True)
    user_set = None





