### Запуск backend:

- Создаем файл .env в корне проекта c параметрами указанными в .env.example:
    - nano .env

- Заменить настройки PostgreSQL на SQLite в файле settings:

# Настройки для sqlite3.
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

- Выполняем запуск:
    python manage.py migrate && python manage.py loaddb && python manage.py runserver
