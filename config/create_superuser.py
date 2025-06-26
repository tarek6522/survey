from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='tarek652').exists():
    User.objects.create_superuser('tarek652', 'tarek@example.com', '27478833')
    print('Superuser created.')
else:
    print('Superuser already exists.')
