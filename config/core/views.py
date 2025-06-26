
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Survey, Question, Reward

def index(request):
    return render(request, 'index.html')

def surveys(request):
    all_surveys = Survey.objects.all()
    return render(request, 'surveys.html', {'surveys': all_surveys})

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def rewards(request):
    all_rewards = Reward.objects.all()
    return render(request, 'rewards.html', {'rewards': all_rewards})

@login_required
def single_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.all()
    return render(request, 'single-survey.html', {'survey': survey, 'questions': questions})

@login_required
def auth_view(request):
    return render(request, 'auth.html')
