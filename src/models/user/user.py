from django.db import models
from ..base import Base

class User(Base, models.Model):
    username = models.CharField(max_length=80, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        db_table = 'user'
        ordering = ['id']

        unique_together = ['email']

    def __str__(self):
        return self.username