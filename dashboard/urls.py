from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('update-points/', views.update_points, name='update_points'),
    path('toggle-active/', views.toggle_user_active, name='toggle_user_active'),


]
