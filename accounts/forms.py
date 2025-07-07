from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'points', 'group']  # هذه الحقول لا يعدلها المستخدم
        labels = {
            'full_name': 'الاسم الكامل',
            'gender': 'الجنس',
            'age': 'العمر',
            'phone': 'رقم الموبايل',
            'city': 'المحافظة',
            'neighborhood': 'الحي / المنطقة',
            'marital_status': 'الحالة الاجتماعية',
            'education': 'المستوى التعليمي',
            'occupation': 'المهنة',
            'employment_status': 'حالة العمل',
            'income': 'متوسط الدخل الشهري',
            'family_members': 'عدد أفراد الأسرة',
            'children': 'عدد الأطفال',
            'health_issues': 'مشاكل صحية (إن وجدت)',
            'interests': 'الاهتمامات',
            'bio': 'نبذة عنك',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'health_issues': forms.Textarea(attrs={'rows': 2}),
            'interests': forms.Textarea(attrs={'rows': 2}),
        }

class CustomLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("تم تعطيل حسابك من قبل الإدارة."),
                code='inactive',
            )
