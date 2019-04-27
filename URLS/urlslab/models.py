from django.conf import settings
from django.db import models
from django.utils import timezone


class Url(models.Model):
    text = models.TextField()

    def shorten(self):
        self.save()

    def __str__(self):
        return self.text
