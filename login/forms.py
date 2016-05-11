# See https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/
from django.forms import ModelForm

from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['school', 'studentID', 'status']
