from atexit import register
import imp
from django.contrib import admin

from .models import Question,Choice
# Register your models here.
#admin.site.register(Question)

@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    list_filter=('pub_date',)
    list_display=('text','pub_date')
    date_hierarchy=('pub_date')
    ordering=('pub_date','text')

admin.site.register(Choice)