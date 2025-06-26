from django.urls import path
from . import views

urlpatterns = [
    path('stats/<int:survey_id>/', views.survey_stats, name='survey_stats'),
    path('', views.surveys, name='surveys'),
    path('single-survey/<int:survey_id>/', views.single_survey, name='single_survey'),
]
