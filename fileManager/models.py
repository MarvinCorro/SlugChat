from django.db import models
from home.models import Course
# 
# Create your models here.
file_dir = './static/uploads/'

class FileDB(models.Model):
	fileObj = models.FileField(upload_to=file_dir)
	fileName = models.CharField(max_length = 20, default='')
	className = models.CharField(max_length = 20, default='')
