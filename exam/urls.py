from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from exam import views

urlpatterns = [
    url(r'^create/',views.create_user,name="create_user"),
    url(r'^login/',views.log_in,name="log_user"),
    url(r'^new_exam/',views.new_exam,name="new_exam"),
    url(r'^add_question/',views.add_question,name="add_question"),
    url(r'^logout',views.log_out,name="log_out"),
    url(r'^exams',views.previous_exams,name="previous_exams"),
    url(r'^(?P<pk>[0-9]+)$',views.question_form,name='question_form'),
    url(r'^(?P<pk>[0-9]+)/results/$',views.results, name="results"),
    url(r'^upload/', views.upload_file, name="upload")

]