
# Survey Site (Django Project)

هذا المشروع عبارة عن منصة استبيانات متكاملة مبنية باستخدام Django.

## الميزات:

- تسجيل المستخدم وتسجيل الدخول.
- عرض الاستبيانات وإرسال الإجابات.
- نظام مكافآت للمستخدمين.
- لوحة إدارة لإدارة الاستبيانات والمكافآت.

## تشغيل المشروع محليًا:

1. إنشاء بيئة افتراضية وتفعيلها:
```bash
python -m venv env
source env/bin/activate   # على لينوكس/ماك
env\Scripts\activate    # على ويندوز
```

2. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

3. إعداد قاعدة البيانات وتشغيل المشروع:
```bash
python manage.py migrate
python manage.py createsuperuser  # لإنشاء مشرف
python manage.py runserver
```

## النشر على Render:

- تأكد من وجود الملفات التالية:
  - `requirements.txt`
  - `Procfile`
  - `render.yaml`

- قم برفع المشروع على GitHub ثم اربطه بحسابك على Render.

