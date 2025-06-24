from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def surveys(request):
    return render(request, 'surveys.html')

def rewards(request):
    return render(request, 'rewards.html')

def contact(request):
    return render(request, 'contact.html')

def auth_view(request):
    return render(request, 'auth.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def single_survey(request):
    return render(request, 'single-survey.html')

