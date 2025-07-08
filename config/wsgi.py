import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

import django
from django.core.management import call_command

django.setup()
try:
    call_command('migrate')
except Exception as e:
    print(f"❌ Migration error: {e}")
