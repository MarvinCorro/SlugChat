from django.contrib import admin

from .models import File
from .models import Comment

admin.site.register(File)
admin.site.register(Comment)