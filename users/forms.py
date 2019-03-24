from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import StudentProfile


class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = StudentProfile
        fields = ['name','school','instructor','email']

