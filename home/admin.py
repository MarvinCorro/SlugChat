from django.contrib import admin

from .models import User, Course, Roster

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Roster)
