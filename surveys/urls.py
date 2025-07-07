from django.urls import path
from . import views
from .views import submit_survey
from .views import reward_dashboard


app_name = 'surveys'  # ✅ هذا السطر ضروري لتفعيل namespace

urlpatterns = [
    path('stats/<int:survey_id>/', views.survey_stats, name='survey_stats'),
    path('', views.surveys, name='survey_list'),  # ✅ يتوافق الآن مع قالب index
    path('single-survey/<int:survey_id>/', views.single_survey, name='single_survey'),
    path('submit/', submit_survey, name='submit_survey'),
    path('dashboard/', reward_dashboard, name='reward_dashboard'),
]
