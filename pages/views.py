from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from surveys.models import Survey, Question
from rewards.models import Reward

def index(request):
    return render(request, 'index.html')



def privacy(request):
    return render(request, 'privacy.html')



def terms(request):
    return render(request, 'terms.html')



def contact(request):
    return render(request, 'contact.html')

@login_required
