from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User                            # we need to mention with which model the form should get associate, because we want to store forms date to model(database)
        fields = ['username','email','first_name','last_name','password1']
        