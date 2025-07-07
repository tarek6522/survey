from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from surveys.models import Survey, Question
from rewards.models import Reward

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    return render(request, 'pages/index.html')



def privacy(request):
    return render(request, 'pages/privacy.html')



def terms(request):
    return render(request, 'pages/terms.html')



def contact(request):
    return render(request, 'pages/contact.html')

@login_required
def placeholder_view(request):
    return render(request, 'pages/placeholder.html')