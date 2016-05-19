from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from login.models import User
from login.forms import UserForm
import os

from .forms import UserForm


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
    profile_pic = request.POST['profile_pic']
    request.session['email_address'] = email_address

    # New user who has never signed in before
    if(not User.objects.filter(email=email_address).exists()):
        user_info = User(firstName=first_name,lastName=last_name,
            email=email_address,profile_pic=profile_pic)
        user_info.save()
    return HttpResponse(status=204)

# See https://docs.djangoproject.com/en/1.9/topics/forms/
# for an explanation of the following code.
def buildprofile(request):
# if this is a POST request we need to process the form data

    email_address = request.session['email_address']

    # If this user's profile is complete, redirect to profile page
    # TODO: move profile page out of login app
    if (not request.GET.get('update', '') == 'true') and User.objects.filter(email=email_address, completeProfile=True).exists():
        return HttpResponseRedirect('/login/profile/')

    instance = User.objects.get(email=email_address)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST, instance=instance)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance.completeProfile = True
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/login/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm(instance=instance)

    return render(request, 'login/buildprofile.html', {'form': form})

def profile(request):
    email_address = request.session['email_address']
    instance = User.objects.get(email=email_address)

    if instance.status == 'ST':
        status = 'Student'
    elif instance.status == 'TA':
        status = 'Teaching Assistant'
    else:
        status = 'Professor'

    context = {'full_name'   : instance.firstName + " " + instance.lastName,
               'school'      : instance.school,
               'studentID'   : instance.studentID,
               'email'       : instance.email,
               'status'      : status,
               'profile_pic' : instance.profile_pic }

    return render(request, 'login/profile.html', context)
