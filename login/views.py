from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from login.models import User
import os

from .forms import ProfileForm

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
    if(not User.objects.filter(firstName=first_name,lastName=last_name,
        email=email_address).exists()):
        user_info = User(firstName=first_name,lastName=last_name,
            email=email_address)
        user_info.save()
    return render(request, 'login/tokensignin.html')

# See https://docs.djangoproject.com/en/1.9/topics/forms/
# for an explanation of the following code.
def buildprofile(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'buildprofile.html', {'form': form})
