from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# روابط الصفحات الأمامية (HTML)
def index(request):
    return render(request, "index.html")

def surveys(request):
    return render(request, 'frontend/surveys.html')

def rewards(request):
    return render(request, 'frontend/rewards.html')

def privacy(request):
    return render(request, 'frontend/privacy.html')

def terms(request):
    return render(request, 'frontend/terms.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def auth_page(request):
    return render(request, 'frontend/auth.html')

def single_survey(request):
    return render(request, 'frontend/single-survey.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),          # الصفحة الرئيسية
    path('surveys/', surveys, name='surveys'),   # استبيانات
    path('rewards/', rewards, name='rewards'),   # مكافآت
    path('privacy/', privacy, name='privacy'),   # سياسة الخصوصية
    path('terms/', terms, name='terms'),         # الشروط والأحكام
    path('contact/', contact, name='contact'),   # صفحة الاتصال
    path('auth/', auth_page, name='auth'),       # صفحة تسجيل الدخول
    path('single-survey/', single_survey, name='single-survey'),  # الاستبيان المفرد
]
