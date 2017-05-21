from django.contrib import admin

from .models import CourseType, Course, Room

# Register your models here.
admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(Room)
