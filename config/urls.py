from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from surveys.views import reward_dashboard
from django.urls import include


from surveys.api import SurveyViewSet, QuestionViewSet, AnswerViewSet
from rewards.api import RewardViewSet, RedemptionRequestViewSet
from accounts.api import UserProfileViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'rewards', RewardViewSet)
router.register(r'redemptions', RedemptionRequestViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # ✅ الآن الصفحة الرئيسية تعمل من pages/views.py > index
    path('surveys/', include('surveys.urls')),
    path('rewards/', include('rewards.urls')),
    path('auth/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('dashboard/', reward_dashboard, name='reward_dashboard'),
    path('admin-dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),


]

handler404 = 'pages.views.custom_404'
