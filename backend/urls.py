from django.contrib import admin
from django.urls import path
from backend.core import views  # تأكد من المسار الصحيح لتطبيقك

urlpatterns = [
    path('', views.index, name='index'),
    path('surveys/', views.surveys, name='surveys'),
    path('surveys/rewards/', views.rewards, name='rewards'),
    path('surveys/contact/', views.contact, name='contact'),
    path('surveys/auth/', views.auth_view, name='auth'),
    path('surveys/privacy/', views.privacy, name='privacy'),
    path('surveys/terms/', views.terms, name='terms'),
    path('surveys/single-survey/', views.single_survey, name='single_survey'),
]
