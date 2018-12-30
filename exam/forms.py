from django import forms
from django.forms import ModelForm
from exam.models import Exam
from django.forms import Widget, RadioSelect


class CreateUser(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class Login(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"login-text"}))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"login-text"}))


class NewExam(forms.Form):
    subjects = (
        ("PSTAR", "PSTAR"),
        ("PPL", "Private Pilots License"),
        ("CPL", "Commercial Pilots Licence"),
        ("IFR", "Instrument Rating"),
        ("ATPL", "Airline Pilots License")
    )
    options = (
        (False, "After each question"),
        (True, "After last question")
    )
    question_amount = forms.IntegerField(max_value=100, widget=forms.NumberInput(attrs={"class":"fields"}))
    subject = forms.ChoiceField(choices=subjects, widget=forms.Select(attrs={"class":"fields"}))
    feedback = forms.ChoiceField(choices=options, widget=forms.Select(attrs={"class":"fields"}))

class OptionSubmit(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(OptionSubmit, self).__init__(*args, **kwargs)
        options = (
            ('a', question.choiceA),
            ('b', question.choiceB),
            ('c', question.choiceC),
            ('d', question.choiceD),
        )

        self.fields['submitted_answer'] = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class": "form-control"}),
                                                            label=question.text, choices=options)

class ContinueQuiz(forms.Form):
    def __init__(self, exam_id, *args, **kwargs):
        super(ContinueQuiz, self).__init__(*args, **kwargs)

        self.fields['exam_id'] = forms.HiddenInput()