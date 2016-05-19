from django import forms
from django.forms import ModelForm
from fileManager.models import FileDB

class FileForm(ModelForm):
	class Meta:
		model = FileDB
		fields = ['fileObj']
