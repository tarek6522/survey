from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from surveys.models import Survey, Question, Answer
from rewards.models import Reward
from accounts.models import UserProfile


# 🔒 دالة مساعدة لضمان وجود الملف الشخصي
def ensure_userprofile(user):
    if user.is_authenticated:
        UserProfile.objects.get_or_create(user=user)


# ✅ تم تأمين الوصول للمستخدمين فقط وإزالة الاستبيانات العامة
@login_required
def surveys(request):
    ensure_userprofile(request.user)
    try:
        group = request.user.userprofile.group
    except AttributeError:
        group = None

    surveys = Survey.objects.filter(target_group=group)

    filter_group = request.GET.get('group')
    sort = request.GET.get('sort')

    if filter_group:
        surveys = surveys.filter(target_group=filter_group)

    if sort == 'points':
        surveys = surveys.order_by('-points')
    elif sort == 'newest':
        surveys = surveys.order_by('-created_at')

    groups = Survey.objects.values_list('target_group', flat=True).distinct()

    return render(request, 'surveys/surveys.html', {
        'surveys': surveys,
        'groups': groups,
        'selected_group': filter_group,
        'selected_sort': sort,
    })


@login_required
def single_survey(request, survey_id):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)
    user_group = getattr(profile, 'group', None)

    # نحاول جلب الاستبيان الذي ينتمي إلى مجموعة المستخدم فقط
    survey = get_object_or_404(Survey, id=survey_id, target_group=user_group)

    questions = survey.questions.prefetch_related('choices').all()
    return render(request, 'surveys/single-survey.html', {
        'survey': survey,
        'questions': questions,
    })



@login_required
def reward_dashboard(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)
    total_points = profile.points

    answered_survey_ids = Answer.objects.filter(user=user).values_list('question__survey', flat=True).distinct()
    answered_surveys = Survey.objects.filter(id__in=answered_survey_ids)

    redemptions = getattr(user, 'redemptionrequest_set', Reward.objects.none()).all()

    return render(request, 'account/dashboard.html', {
        'total_points': total_points,
        'answered_surveys': answered_surveys,
        'redemptions': redemptions,
    })


def survey_stats(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.question_set.all()
    answers_count = Answer.objects.filter(question__survey=survey).count()
    context = {
        'survey': survey,
        'questions': questions,
        'answers_count': answers_count,
    }
    return render(request, 'surveys/stats.html', context)


@csrf_exempt
def submit_survey(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user if request.user.is_authenticated else None

        submitted_questions = []
        for item in data.get('answers', []):
            question_id = item.get('question_id')
            response = item.get('response')
            try:
                question = Question.objects.get(id=question_id)
                Answer.objects.create(
                    question=question,
                    user=user,
                    response=response
                )
                submitted_questions.append(question)
            except Question.DoesNotExist:
                continue

        if user and submitted_questions:
            survey = submitted_questions[0].survey
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.points += survey.points
            profile.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
