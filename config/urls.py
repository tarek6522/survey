
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

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
    path('', include('pages.urls')),
    path('surveys/', include('surveys.urls')),
    path('rewards/', include('rewards.urls')),
    path('auth/', include('accounts.urls')),
    path('api/', include(router.urls)),
]
