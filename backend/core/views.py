from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def surveys(request):
    return render(request, 'surveys.html')

def rewards(request):
    return render(request, 'rewards.html')

def contact(request):
    return render(request, 'contact.html')
