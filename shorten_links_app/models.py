from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    original_url = models.URLField()
    user = models.ManyToManyField(User, related_name='links')

    def __str__(self):
        return f'{self.original_url}'
