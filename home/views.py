from django.shortcuts import render


# Serves the index page for login, which is where the login takes place
# Note that you have to have the key_file.txt in your slugchat directory
# for google login to work.
#
# You must go to localhost:8000/ for login to work, 127.0.0.1:8000/
# will not work due to a Google Sign in requirement.
def index(request):

    try:
        with open('key_file.txt', 'r') as f:
            GOOGLE_KEY = f.read().rstrip()
    except IOError:
        GOOGLE_KEY = None
        print("key_file not found. \nMessage Ckyle for key_file.txt")

    context = {'GOOGLE_KEY': GOOGLE_KEY}
    return render(request, 'home/index.html', context)
