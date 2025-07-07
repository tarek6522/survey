from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from surveys.models import Survey
from accounts.models import UserProfile
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST


@require_POST
@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_points(request):
    user_id = request.POST.get("user_id")
    points = request.POST.get("points")
    
    user = get_object_or_404(User, pk=user_id)
    profile = user.profile
    
    try:
        profile.points = int(points)
        profile.save()
        messages.success(request, f"تم تحديث نقاط {user.username} إلى {points}")
    except:
        messages.error(request, "فشل التحديث. تأكد من صحة البيانات.")
    
    return redirect('dashboard:admin_dashboard')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.select_related("profile").all()
    surveys = Survey.objects.prefetch_related("questions").all()
    return render(request, 'dashboard/dashboard.html', {
        'users': users,
        'surveys': surveys

        
    })

@require_POST
@login_required
@user_passes_test(lambda u: u.is_superuser)
def toggle_user_active(request):
    user_id = request.POST.get("user_id")
    user = get_object_or_404(User, pk=user_id)

    if user.is_superuser:
        messages.error(request, "لا يمكن تعطيل مستخدم يملك صلاحيات مشرف.")
    else:
        user.is_active = not user.is_active
        user.save()
        status = "تم التفعيل" if user.is_active else "تم التعطيل"
        messages.success(request, f"الحساب ({user.username}): {status}")

    return redirect('dashboard:admin_dashboard')
