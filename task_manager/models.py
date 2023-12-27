# task_manager/models.py
from django.db import models


class UserRegistration(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
]

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No'))


class Task1(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(
        choices=TRUE_FALSE_CHOICES, default=0, blank=False)

    def __str__(self):
        return self.title
