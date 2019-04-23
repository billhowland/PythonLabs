from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
