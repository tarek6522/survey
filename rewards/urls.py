from django.urls import path
from . import views

urlpatterns = [
    path('', views.rewards, name='rewards'),  # عرض صفحة المكافآت
    path('request/<int:reward_id>/', views.request_reward, name='request_reward'),  # إرسال طلب استبدال
    path('my-requests/', views.my_reward_requests, name='my_reward_requests'),  # عرض طلبات المستخدم
]
