from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def auth_view(request):
    return render(request, 'auth.html')

def contact_view(request):
    return render(request, 'contact.html')

def privacy_view(request):
    return render(request, 'privacy.html')

def rewards_view(request):
    return render(request, 'rewards.html')

def single_survey_view(request):
    return render(request, 'single-survey.html')

def surveys_view(request):
    return render(request, 'surveys.html')

def terms_view(request):
    return render(request, 'terms.html')

