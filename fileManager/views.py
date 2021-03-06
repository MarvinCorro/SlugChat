import os
from fileManager.models import FileDB
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import file_dir, FileDB
from slugchat.functions import logged_in
from slugchat.settings import MEDIA_ROOT, MEDIA_URL


def upload_file(request, className):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FileForm(initial={'className':className})
	return {'dl_form': form}

def download_file(className):
	files_to_serve = FileDB.objects.filter(className=className)
	files = [(MEDIA_URL + x.fileObj.name, x.fileName) for x in files_to_serve]
	return {'filelist': files}

def generate(request):
	user = logged_in(request)
	if user:
		className = request.GET.get('className', '')
		context = {}
		if user.get_status() == 'Professor':
			context.update(upload_file(request, className))
		context.update(download_file(className))
		return render(request, 'myClassPage.html', context)
	else:
		return HttpResponseRedirect('/')
