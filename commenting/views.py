from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import datetime

from commenting.forms import CommentForm
from .models import File


def index(request):
    #gets a list of all the objects that are commentable
    file_list = File.objects.all()
    #puts object list in a context
    context = {'file_list': file_list,}
    return render(request, 'commenting/index.html', context)


def detail(request, file_id):
    #fetches an object from the list of objects
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pub_date = datetime.now
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'commenting/detail.html', {'file':file, 'form': form})
