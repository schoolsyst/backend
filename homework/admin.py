from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register, ModelAdmin
from .models import *
from common.utils import auto_list_display

@register(Grade)
class GradeAdmin(ModelAdmin):
    list_display = ('uuid', 'subject', 'name', 'obtained', 'expected', 'goal', 'weight', 'unit', 'added')
    list_editable = ('name', 'obtained', 'expected', 'goal', 'weight', 'unit')

@register(Homework)
class HomeworkAdmin(ModelAdmin):
    list_display = ('uuid', 'subject', 'name', 'due', 'progress', 'type', 'added')
    list_editable = ('name', 'progress', 'type')
