from __future__ import unicode_literals

from django.db import models

DAY_CHOICES = (
    ('Lundi', 'Lundi'),
    ('Mardi', 'Mardi'),
    ('Mercredi', 'Mercredi'),
    ('Jeudi', 'Jeudi'),
    ('Vendredi', 'Vendredi'),
    ('Samedi', 'Samedi'),
    ('Dimanche', 'Dimanche'),
)


# Create your models here.
class CourseType(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=150)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=150, default="Paris")

    def __str__(self):
        return self.street


class Room(models.Model):
    name = models.CharField(max_length=150)
    address = models.ForeignKey(Address)

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
