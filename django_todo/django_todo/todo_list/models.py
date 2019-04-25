from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def complete(self):
        self.completed = not self.completed
        # if self.completed:
        #     self.completed_date = ''
        self.save()

    def __str__(self):
        return self.text
