from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    original_url = models.URLField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.original_url}'
