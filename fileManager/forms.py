from django.forms import ModelForm
from fileManager.models import FileDB

class FileForm(ModelForm):
	title = forms.CharField(max_length=50)
    fileObj = forms.FileField()
	class Meta:
		model = FileDB
		fields = ['name', 'uploader', 'date', 'fileObj']
