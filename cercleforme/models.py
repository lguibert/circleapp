from __future__ import unicode_literals

import datetime
from django.db import models

DAY_CHOICES = (
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
    ('SU', 'Sunday'),
)


# Create your models here.
class CourseType(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(CourseType)
    room = models.ForeignKey(Room)
    day = models.CharField(max_length=150, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
