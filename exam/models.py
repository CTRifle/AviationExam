from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
import random
from django.db.models import Case, When
from django.template.defaultfilters import truncatechars

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
    incorrect_questions = models.CharField(max_length=200, validators=[validate_comma_separated_integer_list],
                                           default='')
    incorrect_answers = models.CharField(max_length=200, default='')
    current_question = models.IntegerField(default=0)
    answer_at_end = models.BooleanField(default=True)
    score = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)

    # sets a question list that is saved in the model for later.
    # It creates a list of all question IDs in the DB, then selects random ones and saves to the question order
    def set_questions(self):
        my_ids = Question.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        n = int(self.question_amount)
        list_ids = random.sample(my_ids, n)
        self.question_order = str(list_ids).strip("[").strip("]")
        self.save()

    # returns the question object using the PK as an individual question object based on what question the user is on
    def get_question(self):
        question_list = self.question_order.split(",")
        question_id = question_list[self.current_question]
        question_object = Question.objects.get(id=question_id)
        return question_object

    # takes the string from the field and makes it into a list to get a list of objects that the user answered incorrectly
    def get_incorrect_questions(self):
        pk_list = self.incorrect_questions.split(",")
        del pk_list[0]
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
        incorrect_questions = Question.objects.filter(pk__in=pk_list).order_by(preserved)

        return incorrect_questions

    # takes a string of the wrong selected option (ie a,b,c,d) which are kept in order, and puts them in a list
    def get_incorrect_answers(self): ## Returns a list of the wrong answers in order
        wrong_answer_list = self.incorrect_answers.split(",")
        del wrong_answer_list[0]
        return wrong_answer_list

    def result_message(self):
        fail_message = "You need to review some more, see below for study topics."
        pass_message = "You are over the pass mark for the PSTAR exam, good job!"
        if self.score == 0:
            return fail_message
        elif ((self.score/self.question_amount) * 100) < 90:
            return fail_message
        else:
            return pass_message

    def result_percentage(self):
        return round(((self.score/self.question_amount) * 100))

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
    topic = (
        ("CA", "Collision Avoidance"),
        ("VS", "Visual Signals"),
        ("COMM", "Communications"),
        ("ADS", "Aerodromes"),
        ("EQIP", "Equipment"),
        ("PR", "Pilot Responsibilities"),
        ("WT", "Wake Turbulence"),
        ("AMED","Aeromedical"),
        ("FPL", "Flight Plans and Itineraries"),
        ("ATC", "Clearances and Instructions"),
        ("AOPS", "Aircraft Operations"),
        ("REGS", "Regulations - General Airspace"),
        ("ASPC", "Controlled Airspace"),
        ("SFTY", "Aviation Occurrences")
    )

    text = models.CharField(max_length=1000)
    topic = models.CharField(max_length=30, default="", choices=topic)
    choiceA = models.CharField(max_length=1000)
    choiceB = models.CharField(max_length=1000)
    choiceC = models.CharField(max_length=1000)
    choiceD = models.CharField(max_length=1000)
    answer_text = models.CharField(max_length=1000, blank=True)
    answer = models.CharField(max_length=100, default='a', choices=answers)
    subject = models.CharField(max_length=100, default='', choices=subjects)
    context = models.CharField(max_length=1000, default="")


    def __str__(self):
        return self.text

    @property
    def short_text(self):
        return truncatechars(self.text, 100)




