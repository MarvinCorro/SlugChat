from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    try:
        with open('key_file.txt', 'r') as f:
            GOOGLE_KEY = f.read().rstrip()
    except IOError:
        GOOGLE_KEY = None
        print("key_file not found. \nMessage Ckyle for key_file.txt")
    context = {'GOOGLE_KEY' : GOOGLE_KEY }
    return render(request, 'login/index.html', context)
