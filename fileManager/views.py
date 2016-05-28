import os
from fileManager.models import FileDB
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import file_dir, FileDB
from slugchat.settings import MEDIA_ROOT

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
	new_dir = MEDIA_ROOT + file_dir
	files = ['media_cdn/static/uploads/'+x for x in os.listdir(new_dir)]
	return render(request, 'download.html', {'filelist': files})
