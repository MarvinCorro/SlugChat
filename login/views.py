from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def tokensignin(request):
    id_token = request.POST['idtoken']
    print(id_token)
    return render(request, 'login/tokensignin.html')
