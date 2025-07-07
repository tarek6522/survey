from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# خيارات للاستخدام في نموذج UserProfile
GENDER_CHOICES = [
    ('male', 'ذكر'),
    ('female', 'أنثى'),
]

MARITAL_STATUS_CHOICES = [
    ('single', 'أعزب / عزباء'),
    ('married', 'متزوج / متزوجة'),
    ('divorced', 'مطلّق / مطلّقة'),
    ('widowed', 'أرمل / أرملة'),
]

EDUCATION_CHOICES = [
    ('none', 'دون تعليم'),
    ('primary', 'ابتدائي'),
    ('middle', 'إعدادي'),
    ('highschool', 'ثانوي'),
    ('diploma', 'معهد'),
    ('bachelor', 'بكالوريوس'),
    ('master', 'ماجستير'),
    ('phd', 'دكتوراه'),
]

INCOME_CHOICES = [
    ('none', 'لا يوجد دخل'),
    ('<100k', 'أقل من 100 ألف ل.س'),
    ('100k-300k', 'بين 100 ألف - 300 ألف ل.س'),
    ('300k-600k', 'بين 300 ألف - 600 ألف ل.س'),
    ('>600k', 'أكثر من 600 ألف ل.س'),
]

CITIES = [
    ('damascus', 'دمشق'),
    ('aleppo', 'حلب'),
    ('homs', 'حمص'),
    ('hama', 'حماة'),
    ('latakia', 'اللاذقية'),
    ('tartous', 'طرطوس'),
    ('daraa', 'درعا'),
    ('sweida', 'السويداء'),
    ('deir-ezzor', 'دير الزور'),
    ('raqqa', 'الرقة'),
    ('idlib', 'إدلب'),
    ('hasakeh', 'الحسكة'),
    ('quneitra', 'القنيطرة'),
    ('rural-damascus', 'ريف دمشق'),
    ('other', 'أخرى'),
]

# نموذج البروفايل الكامل
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # نظام النقاط والمجموعة (كما كان سابقاً)
    points = models.IntegerField(default=0)
    group = models.CharField(max_length=100, blank=True, null=True)

    # معلومات المستخدم الشخصية والاجتماعية
    full_name = models.CharField("الاسم الكامل", max_length=150, blank=True)
    gender = models.CharField("الجنس", max_length=10, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField("العمر", blank=True, null=True)
    phone = models.CharField("رقم الموبايل", max_length=15, blank=True, null=True)
    city = models.CharField("المحافظة", max_length=50, choices=CITIES, blank=True)
    neighborhood = models.CharField("الحي / المنطقة", max_length=100, blank=True)
    marital_status = models.CharField("الحالة الاجتماعية", max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True)
    education = models.CharField("المستوى التعليمي", max_length=20, choices=EDUCATION_CHOICES, blank=True)
    occupation = models.CharField("المهنة", max_length=100, blank=True)
    employment_status = models.CharField("حالة العمل", max_length=100, blank=True)
    income = models.CharField("متوسط الدخل الشهري", max_length=50, choices=INCOME_CHOICES, blank=True)
    family_members = models.PositiveIntegerField("عدد أفراد الأسرة", blank=True, null=True)
    children = models.PositiveIntegerField("عدد الأطفال", blank=True, null=True)
    health_issues = models.TextField("مشاكل صحية إن وجدت", blank=True)
    interests = models.TextField("الاهتمامات الشخصية", blank=True)
    bio = models.TextField("نبذة عنك", blank=True)

    def __str__(self):
        return f"الملف الشخصي لـ {self.user.username}"

# إشارة لإنشاء ملف شخصي تلقائيًا عند إنشاء مستخدم
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()
