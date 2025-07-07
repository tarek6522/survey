from django.urls import path
from . import views  # ✅ لاستيراد auth_view و dashboard
from .views import auth_view, dashboard, logout_view  # ✅ تأكد من إضافة logout_view
from .views import edit_profile  # ✅ تأكد من الاستيراد


app_name = 'accounts'

urlpatterns = [
    path('auth/', views.auth_view, name="auth"),  # ✅ العرض الصحيح لصفحة auth
    path('dashboard/', views.dashboard, name="dashboard"),  # ✅ لوحة التحكم
    path('logout/', logout_view, name='logout'),
    path('profile/', edit_profile, name='edit_profile'),  # ✅ تعديل الملف الشخصي


]
