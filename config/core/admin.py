from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

from .models import Survey, Question, Answer, Reward, RedemptionRequest

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class RedemptionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'reward', 'status', 'requested_at')
    list_filter = ('status', 'requested_at')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(is_approved=True)
    approve_requests.short_description = "قبول الطلبات المحددة"

    def reject_requests(self, request, queryset):
        queryset.update(is_approved=False)
    reject_requests.short_description = "رفض الطلبات المحددة"

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Reward)
admin.site.register(RedemptionRequest, RedemptionRequestAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answered_at')
    search_fields = ('user__username', 'question__text')
    list_filter = ('answered_at',)

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
