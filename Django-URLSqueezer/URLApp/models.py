# from django.conf import settings
from django.db import models
# from django.utils import timezone


class Shrink(models.Model):
    long_url = models.CharField(max_length=500, unique=True)
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.long_url
