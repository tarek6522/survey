import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# ✅ تحديد BASE_DIR لحساب موقع staticfiles
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ إعداد متغير البيئة
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# ✅ تفعيل التطبيق الأساسي
application = get_wsgi_application()

# ✅ تمكين Whitenoise لخدمة ملفات static من staticfiles
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
