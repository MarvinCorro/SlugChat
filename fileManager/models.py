from django.db import models

# 
# Create your models here.
file_dir = './user_files/'

class FileDB(models.Model):
	fileObj = models.FileField(upload_to=file_dir)
	