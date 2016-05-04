from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
	course = "course"
	context = {'course':course,}
	return render(request, 'chat/index.html', context)
    
def class_chat(request):
	return render(request, 'chat/class_chat.html')