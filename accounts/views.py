from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_backends
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
import re

from surveys.models import Survey, Answer
from rewards.models import RedemptionRequest
from accounts.models import UserProfile
from .forms import UserProfileForm

def auth_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email=email)

                if not user.is_active:
                    messages.error(request, '⚠️ تم تعطيل حسابك من قبل الإدارة، لا يمكنك الدخول حالياً.')
                    return redirect('accounts:auth')

                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    backend = get_backends()[0]
                    user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                    login(request, user)
                    return redirect('accounts:dashboard')
                else:
                    messages.error(request, 'بيانات الدخول غير صحيحة.')
            except User.DoesNotExist:
                messages.error(request, 'لا يوجد حساب مرتبط بهذا البريد الإلكتروني.')

        elif form_type == 'signup':
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            phone = request.POST.get('phone')

            if not re.fullmatch(r'09\d{8}', phone):
                messages.error(request, 'يرجى إدخال رقم هاتف سوري صحيح (يبدأ بـ 09 ويتكون من 10 أرقام).')
            elif password != confirm_password:
                messages.error(request, 'كلمتا المرور غير متطابقتين.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'هذا البريد الإلكتروني مستخدم مسبقاً.')
            else:
                username = email.split('@')[0]
                user = User.objects.create_user(username=username, email=email, password=password)

                profile, _ = UserProfile.objects.get_or_create(user=user)
                profile.phone = phone
                profile.save()

                backend = get_backends()[0]
                user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                login(request, user)
                return redirect('accounts:dashboard')

    return render(request, 'accounts/auth.html')


@login_required
def dashboard(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    answers = Answer.objects.filter(user=user).select_related('question__survey')
    redemptions = RedemptionRequest.objects.filter(user=user)

    unique_surveys = {a.question.survey for a in answers if hasattr(a.question.survey, 'points')}
    total_points = sum([s.points for s in unique_surveys])

    available_surveys = Survey.objects.filter(
        models.Q(is_public=True) | models.Q(target_group=profile.group)
    ).distinct()

    context = {
        'total_points': total_points,
        'answers': answers,
        'redemptions': redemptions,
        'available_surveys': available_surveys,
    }

    return render(request, 'account/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:auth')


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ تم حفظ التعديلات بنجاح.')
            return redirect('accounts:edit_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'account/profile.html', {'form': form})
