from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from surveys.models import Survey, Question
from rewards.models import Reward
from surveys.models import Answer  # تأكد من أن Answer موجود في models

def surveys(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        group = request.user.userprofile.group
    else:
        group = None

    surveys = Survey.objects.filter(
        models.Q(is_public=True) | models.Q(target_group=group)
    )
    return render(request, 'surveys/surveys.html', {'surveys': surveys})


def single_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.all()
    return render(request, 'surveys/single-survey.html', {'survey': survey, 'questions': questions})


@login_required
def reward_dashboard(request):
    return render(request, 'accounts/dashboard.html')  # ✅ تم تصحيحه


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
