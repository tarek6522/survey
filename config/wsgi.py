import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# ✅ تمكين whitenoise لخدمة staticfiles مباشرة
from whitenoise import WhiteNoise
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

