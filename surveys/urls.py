from django.urls import path
from . import views

app_name = 'surveys'  # ✅ هذا السطر ضروري لتفعيل namespace

urlpatterns = [
    path('stats/<int:survey_id>/', views.survey_stats, name='survey_stats'),
    path('', views.surveys, name='survey_list'),  # ✅ يتوافق الآن مع قالب index
    path('single-survey/<int:survey_id>/', views.single_survey, name='single_survey'),
]
