from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from login.models import User
from login.models import Roster
from login.models import Course
from login.forms import UserForm
from login.forms import RosterForm
from login.forms import CourseForm

from login.functions import logged_in


# Serves the index page for login, which is where the login takes place
# Note that you have to have the key_file.txt in your slugchat directory
# for google login to work.
#
# You must go to localhost:8000/login/ for login to work, 127.0.0.1:8000/login
# will not work.
def index(request):
    try:
        with open('key_file.txt', 'r') as f:
            GOOGLE_KEY = f.read().rstrip()
    except IOError:
        GOOGLE_KEY = None
        print("key_file not found. \nMessage Ckyle for key_file.txt")
    context = {'GOOGLE_KEY': GOOGLE_KEY}
    return render(request, 'login/index.html', context)


# This is the function that takes the info from google sign in, then adds the
# user to the database if they are not already in the database. The
# request.session key 'email_address' is also set in this function, which is
# the backbone of the login system.
@csrf_exempt
def tokensignin(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email_address']
    profile_pic = request.POST['profile_pic']
    request.session['email_address'] = email_address

    # New user who has never signed in before
    if(not User.objects.filter(email=email_address).exists()):
        user_info = User(firstName=first_name, lastName=last_name,
                         email=email_address, profile_pic=profile_pic)
        user_info.save()
    return HttpResponse(status=204)


# Displays the profile information for the user.
def profile(request):

    if not logged_in(request):
        return HttpResponseRedirect('/login/')

    email_address = request.session['email_address']
    instance = User.objects.get(email=email_address)
    # Here we grab all the courses that the current user has enrolled in
    rosters = instance.roster_set.all()

    context = {'full_name': instance.firstName + " " + instance.lastName,
               'school': instance.school,
               'studentID': instance.studentID,
               'email': instance.email,
               'status': instance.get_status(),
               'profile_pic': instance.profile_pic,
               'classes': rosters.all()
               }

    return render(request, 'login/profile.html', context)


# This page allows a user to update fields in their user profile.
# Interactions with the db are done using model forms, which take
# care of building the forms to display.
#
# The user comes to this page in one of two ways. First, when they fist log
# in to our app, they will be directed here to complete their profile. Second,
# they can go to /buildprofile/?update=true and they will be able to update
# their profile again.
#
# user_form is sent to the template, it contains the fields:
#   firstName, lastName, profile_pic, school, studentID, and status.
def buildprofile(request):

    if not logged_in(request):
        return HttpResponseRedirect('/login/')

    email_address = request.session['email_address']

    # If this user's profile is complete, and they aren't coming here to
    # update their profile, redirect to profile page
    if (not request.GET.get('update', '') == 'true' and
            User.objects.filter(
            email=email_address, completeProfile=True).exists()):
        return HttpResponseRedirect('/login/profile/')

    # We get the current user and assign it to the user variable, then
    # tell the model form that we want to update the information for
    # this user.
    user = User.objects.get(email=email_address)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.completeProfile = True
            user_form.save()
            return HttpResponseRedirect('/login/profile/')
    else:
        user_form = UserForm(instance=user)
    return render(request, 'login/buildprofile.html',
                  {'user_form': user_form})


# Only professors can add a class.
def addclass(request):

    if not logged_in(request):
        return HttpResponseRedirect('/login/')

    email_address = request.session['email_address']

    user = User.objects.get(email=email_address)
    if not (User.objects.filter(
            email=email_address, status="PR").exists()):
        return HttpResponse('Sorry, only professors can add classes.')

    course = Course(professor=user)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            return HttpResponseRedirect('/login/profile/')

    else:
        course_form = CourseForm()

    return render(request, 'login/addclass.html',
                  {'course_form': course_form})


# Only students can enroll in a course.
def enroll(request):

    if not logged_in(request):
        return HttpResponseRedirect('/login/')

    email_address = request.session['email_address']

    user = User.objects.get(email=email_address)
    if not (User.objects.filter(
            email=email_address, status="ST").exists()):
        return HttpResponse('Sorry, only students may sign up for classes.')

    roster = Roster(studentID=user)
    if request.method == 'POST':
        roster_form = RosterForm(request.POST, instance=roster)
        if roster_form.is_valid():
            roster_form.save()
            return HttpResponseRedirect('/login/profile/')

    else:
        roster_form = RosterForm()

    return render(request, 'login/enroll.html',
                  {'roster_form': roster_form})
