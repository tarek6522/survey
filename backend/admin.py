
from django.contrib import admin
from .models import Survey, Question, Answer, Reward, RedemptionRequest

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class RedemptionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'reward', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
    approve_requests.short_description = "قبول الطلبات المحددة"

    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
    reject_requests.short_description = "رفض الطلبات المحددة"

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
admin.site.register(Reward)
admin.site.register(RedemptionRequest, RedemptionRequestAdmin)
