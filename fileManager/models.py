from django.db import models

# https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/
# Create your models here.
class FileDB(models.Model):
	name = models.CharField(max_length=50)
	uploader = models.CharField(max_length=50)
	date = models.CharField(max_length=50)
	fileObj = models.FileField(upload_to='/tmp/')
	