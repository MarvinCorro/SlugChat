from django import forms

class ProfileForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
