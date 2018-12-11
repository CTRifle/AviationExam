from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
import random


class Exam(models.Model):
    subjects = (
        ("PSTAR","PSTAR"),
        ("PPL","Private Pilots License"),
        ("CPL","Commercial Pilots Licence"),
        ("IFR","Instrument Rating"),
        ("ATPL","Airline Pilots License")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, default='', choices=subjects)
    question_amount = models.IntegerField(default=10)
    question_order = models.CharField(max_length=200, validators=[validate_comma_separated_integer_list], default='')
    incorrect_questions = models.CharField(max_length=200, validators=[validate_comma_separated_integer_list], default='')
    current_question = models.IntegerField(default=0)
    answer_at_end = models.BooleanField(default=True)
    score = models.IntegerField(default=0)

    def set_questions(self):
        ques_ids = random.sample(range(1, Question.objects.latest('id').id), int(self.question_amount))
        self.question_order = str(ques_ids).strip('[').strip(']').strip("'").replace(' ','')
        self.save()

    # returns the question object using the PK, and sends it to the related view.
    def get_question(self):
        question_list = self.question_order.split(",")
        question_id = question_list[self.current_question]
        question_object = Question.objects.get(id=question_id)
        return question_object

    def get_incorrect_questions(self):
        question_list = self.incorrect_questions.split(",")
        del question_list[0]
        object = Question.objects.filter(id__in=question_list)
        return object


    def __str__(self):
        return "Exam" + str(self.pk) + "-" + str(self.subject)

class Question(models.Model):
    subjects = (
        ("PSTAR", "PSTAR"),
        ("PPL", "Private Pilots License"),
        ("CPL", "Commercial Pilots Licence"),
        ("IFR", "Instrument Rating"),
        ("ATPL", "Airline Pilots License")
    )
    answers = (
        ("a", "A"),
        ("b", "B"),
        ("c", "C"),
        ("d", "D"),
    )
    text = models.CharField(max_length=100)
    choiceA = models.CharField(max_length=100)
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100)
    choiceD = models.CharField(max_length=100)
    answer_text = models.CharField(max_length=1000, blank=True)
    answer = models.CharField(max_length=100, default='a', choices=answers)
    subject = models.CharField(max_length=100, default='', choices=subjects)

    def __str__(self):
        return self.text



