from typing import override

from django.contrib.auth.models import User
from django.db import models

# - Browse events with filters (by date, category, or location).
# - Event submission (title, date, category, location, description).
# - View event details.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Events(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['date']
    
    def __str__(self) -> str:
        return self.title
    
    
