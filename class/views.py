from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from home.models import User
from slugchat.functions import logged_in


def class_chat(request):
        if not logged_in(request):
            return HttpResonseRedirect('/')

        user = User.objects.get(email=request.session['email_address'])
        context = {'firstname': user.firstName,
                   'currentclass': request.GET.get('class', '')}
        #return render(request, 'class/class_chat.html', context)
        return render(request, 'class/mainAppPage.html', context)
