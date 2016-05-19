from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from login.models import User
from login.forms import UserForm
from login.forms import RosterForm
from login.forms import CourseForm


def index(request):
    try:
        with open('key_file.txt', 'r') as f:
            GOOGLE_KEY = f.read().rstrip()
    except IOError:
        GOOGLE_KEY = None
        print("key_file not found. \nMessage Ckyle for key_file.txt")
    context = {'GOOGLE_KEY': GOOGLE_KEY}
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
        user_info = User(firstName=first_name, lastName=last_name,
                         email=email_address, profile_pic=profile_pic)
        user_info.save()
    return HttpResponse(status=204)


# See https://docs.djangoproject.com/en/1.9/topics/forms/
# for an explanation of the following code.
def buildprofile(request):

    email_address = request.session['email_address']

    # If this user's profile is complete, redirect to profile page
    if (not request.GET.get('update', '') == 'true' and
            User.objects.filter(
            email=email_address, completeProfile=True).exists()):
        return HttpResponseRedirect('/login/profile/')

    instance = User.objects.get(email=email_address)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=instance)
        roster_form = RosterForm(request.POST)
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.professor = instance
            course_form.save()
        if roster_form.is_valid():
            roster_form.studentID = instance
            roster_form.save()

        if user_form.is_valid():
            instance.completeProfile = True
            user_form.save()
            return HttpResponseRedirect('/login/profile/')

    else:
        user_form = UserForm(instance=instance)
        roster_form = RosterForm()
        course_form = CourseForm()

    return render(request, 'login/buildprofile.html',
                  {'user_form': user_form, 'roster_form': roster_form,
                   'course_form': course_form})


def profile(request):
    email_address = request.session['email_address']
    instance = User.objects.get(email=email_address)
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
