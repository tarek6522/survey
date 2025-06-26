from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from surveys.models import Survey, Question
from rewards.models import Reward

def auth_view(request):
    return render(request, 'auth.html')

from surveys.models import Survey, Answer
from rewards.models import RedemptionRequest

@login_required
def dashboard(request):
    user = request.user
    answers = Answer.objects.filter(user=user)
    redemptions = RedemptionRequest.objects.filter(user=user)
    total_points = sum([a.survey.points for a in answers if hasattr(a.survey, 'points')])
    context = {
        'total_points': total_points,
        'answers': answers,
        'redemptions': redemptions,
    }
    return render(request, 'accounts/dashboard.html', context)
