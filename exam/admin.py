from django.contrib import admin
from exam.models import Exam, Question


admin.site.register(Exam)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'subject', 'topic')
    list_display_links = ('id', 'short_text')
    search_fields = ('text', 'subject')

admin.site.register(Question, QuestionAdmin)