from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from login.models import User
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
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email_address']
    print(first_name, last_name, email_address)
    user_info = User(firstName=first_name,lastName=last_name,
        email=email_address)
    user_info.save()
    return render(request, 'login/tokensignin.html')

