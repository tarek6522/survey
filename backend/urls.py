
from django.contrib import admin
from django.urls import path
from backend.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('auth/', views.auth_view, name='auth'),
    path('contact/', views.contact_view, name='contact'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('rewards/', views.rewards_view, name='rewards'),
    path('survey/', views.single_survey_view, name='single_survey'),
    path('surveys/', views.surveys_view, name='surveys'),
    path('terms/', views.terms_view, name='terms'),
]
