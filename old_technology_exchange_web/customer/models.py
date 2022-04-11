from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.


class User(AbstractUser):
    sex_choices = ((0, 'Male'), (1, 'Female'), (2, 'Unknown'))
    gender = models.IntegerField(choices=sex_choices, default=2)
    phone_number = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=255, default='', blank=True)
    avatar = models.CharField(max_length=255, default='')
