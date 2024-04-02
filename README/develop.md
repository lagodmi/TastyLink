для запуска в режиме разработки.
- заменить настройки PostgreSQL в файле settings

# Настройки для sqlite3.
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

- запустить backend

    python manage.py migrate && python manage.py loaddb && python manage.py runserver

