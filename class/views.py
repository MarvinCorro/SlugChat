from django.http import HttpResponseRedirect
from django.shortcuts import render
from slugchat.functions import logged_in


def class_chat(request):
        user = logged_in(request)
        if user is None:
            return HttpResponseRedirect('/')

        context = {'firstname': user.firstName,
                   'currentclass': request.GET.get('class', '')}
        return render(request, 'class/class_chat.html', context)
