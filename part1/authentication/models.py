from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MALE = "m"
    FEMALE = "f"
    SEX = [(MALE, "Male"), (FEMALE, "Female")]

    UNKNOWN = "unknown"
    EMPLOYEE = "employee"
    HR = "hr"
    ROLE = [(UNKNOWN, "unknown"), (EMPLOYEE, "employee"), (HR, "hr")]

    sex = models.CharField(max_length=1, choices=SEX)
    role = models.CharField(max_length=8, choices=ROLE, default=UNKNOWN)
