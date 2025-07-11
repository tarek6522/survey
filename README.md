# 📊 منصة الاستبيانات التفاعلية

منصة ويب متكاملة لإنشاء وتعبئة الاستبيانات، وكسب النقاط، واسترداد المكافآت. مصممة باستخدام Django وHTMX وChart.js.

---

## 🚀 الميزات الرئيسية

- ✅ تسجيل المستخدمين وتخصيص مجموعاتهم
- ✅ استبيانات ديناميكية يتم عرضها تلقائيًا سؤالًا تلو الآخر
- ✅ لوحة تحكم للمستخدم تظهر النقاط والإجابات والطلبات
- ✅ صفحة إحصائية برسوم بيانية (Pie/Bar) باستخدام Chart.js
- ✅ نظام صلاحيات لعرض استبيانات حسب المجموعة أو العلنية
- ✅ واجهة مشرف رسومية لإدارة الأسئلة والاستبيانات دون الحاجة لـ Django Admin
- ✅ دعم PostgreSQL وواجهة نشر جاهزة على Render

---

## 🛠️ تثبيت وتشغيل المشروع محليًا

```bash
# 1. إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # في ويندوز: venv\Scripts\activate

# 2. تثبيت المتطلبات
pip install -r requirements.txt

# 3. إعداد قاعدة البيانات
python manage.py migrate

# 4. إنشاء مستخدم مسؤول
python manage.py createsuperuser

# 5. تشغيل الخادم
python manage.py runserver
```

---

## 🌐 النشر على Render

> إعداد مسبق في ملف `render.yaml`  
فقط اربط المشروع بحساب GitHub ثم اختر:
- Build Command: `pip install -r requirements.txt && python manage.py migrate`
- Start Command: `gunicorn backend.wsgi`

---

## 🧪 الاستخدام

### 📥 تعبئة استبيان
- يدخل المستخدم ويسجّل
- يرى الاستبيانات المسموحة له (حسب الصلاحيات)
- يجيب على الأسئلة تلقائيًا واحدة تلو الأخرى

### 🎁 استرداد المكافآت
- من لوحة التحكم، يقدم طلب استرداد
- المشرف يقبل أو يرفض الطلب من لوحة Django أو عبر تعديل الحالة

---

## 📊 الإحصاءات

تُعرض لكل استبيان عبر صفحة `/surveys/stats/<id>/`  
وتشمل:
- عدد الإجابات الكلي
- توزيع الإجابات لكل سؤال (Pie + Bar Chart)

---

## 👨‍💼 لوحة المشرف

المسار: `/admin-panel/`  
المميزات:
- عرض كل الاستبيانات
- إدارة الأسئلة (إضافة – تعديل – حذف) داخل صفحة واحدة
- عرض الإحصاءات برسوم بيانية لكل استبيان
- متاحة فقط للمستخدمين `is_staff=True`

---

## 🧩 التقنيات المستخدمة

- Django + PostgreSQL
- HTMX (تفاعل فوري بدون JavaScript معقد)
- Chart.js (رسوم بيانية ديناميكية)
- TailwindCSS (تصميم عصري وأنيق)
- Render (للنشر السريع)

---

## 📸 صور توضيحية (يمكن إضافتها لاحقًا)

```
📷 صورة: تعبئة سؤال تفاعلي
📷 صورة: لوحة تحكم المستخدم
📷 صورة: رسم بياني لنتائج استبيان
📷 صورة: واجهة إدارة الأسئلة
```

---

تم تطوير هذا المشروع بإتقان ليناسب الإنتاج مباشرة 🎯
# تعديل بسيط لتفعيل إعادة النشر على Render
