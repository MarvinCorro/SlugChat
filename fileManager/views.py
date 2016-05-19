import os
from fileManager.models import FileDB
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import file_dir, FileDB

@csrf_protect
def upload_file(request):
	if request.method == 'POST':
		print('is post :)')
		form = FileForm(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			print('saving!')
			form.save()
			return HttpResponseRedirect('/chat/')
		else:
			print("form not valid :(")
	else:
		print('is not post :(')
		form = FileForm()
	return render(request, 'upload.html', {'form': form})

def download_file(request):
	files = [file_dir+x for x in os.listdir(file_dir)]
	return render(request, 'download.html', {'filelist': files})
