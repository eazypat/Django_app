from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s' % (self.name, self.email)