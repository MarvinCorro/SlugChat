from django.db import models

# 
# Create your models here.
file_dir = '/static/uploads/'

class FileDB(models.Model):
	fileObj = models.FileField(upload_to=file_dir)
