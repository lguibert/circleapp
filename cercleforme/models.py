from __future__ import unicode_literals

from django.db import models


# Create your models here.
class CourseTypes(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)


