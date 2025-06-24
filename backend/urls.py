from django.contrib import admin
from django.urls import path
from backend.core import views  # تأكد من المسار الصحيح لتطبيقك

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('surveys/', views.surveys, name='surveys'),
    path('surveys/rewards/', views.rewards, name='rewards'),
    path('surveys/contact/', views.contact, name='contact'),
]
