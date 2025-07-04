from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from surveys.models import Survey, Question
from rewards.models import Reward

def rewards(request):
    all_rewards = Reward.objects.all()
    return render(request, 'rewards/rewards.html', {'rewards': all_rewards})

@login_required
def dummy_view(request):
    return render(request, 'accounts/dashboard.html')  # ✅ تم تعديل المسار
