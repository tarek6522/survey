from django.contrib import admin
from .models import Survey, Question, Answer  # تأكد من استيراد جميع الموديلات التي تريدها

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
