from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from surveys.models import Survey, Question
from rewards.models import Reward, RedemptionRequest
from accounts.models import UserProfile  # ضروري لجلب النقاط

# ✅ عرض صفحة جميع المكافآت
def rewards(request):
    all_rewards = Reward.objects.all()
    return render(request, 'rewards/rewards.html', {'rewards': all_rewards})

# ✅ دالة مؤقتة (قد تزال لاحقًا)
@login_required
def dummy_view(request):
    return render(request, 'accounts/dashboard.html')

# ✅ عرض طلبات المكافآت الخاصة بالمستخدم
@login_required
def my_reward_requests(request):
    requests = RedemptionRequest.objects.filter(user=request.user).select_related('reward').order_by('-requested_at')
    return render(request, 'rewards/my_requests.html', {'requests': requests})

# ✅ دالة إرسال طلب استبدال المكافأة
@login_required
def request_reward(request, reward_id):
    reward = get_object_or_404(Reward, id=reward_id)
    profile = UserProfile.objects.get_or_create(user=request.user)[0]  # ✅ تعديل آمن لتفادي الخطأ

    if request.method == "POST":
        if profile.points >= reward.points_required:
            # خصم النقاط
            profile.points -= reward.points_required
            profile.save()

            # إنشاء طلب المكافأة
            RedemptionRequest.objects.create(user=request.user, reward=reward)
            messages.success(request, "تم إرسال طلب المكافأة بنجاح.")
        else:
            messages.error(request, "لا تملك نقاط كافية لهذه المكافأة.")
    return redirect("rewards")
