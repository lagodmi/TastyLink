### Запуск backend:

- Создаем файл .env в корне проекта c параметрами указанными в .env.example
    - nano .env
    - установить DEBUG=True

- Заменить настройки PostgreSQL на SQLite в файле settings (при необходимости):

```python
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
```

- создать и запустить виртуальное окружение:
```python3 -m venv venv && source venv/bin/activate```

- установить зависимости:
```
cd backend/foodgram/ && pip install -r requirements.txt
```

- Выполняем запуск:
```python manage.py migrate && python manage.py loaddb && python manage.py runserver```

- [Документация по работе с API](http://127.0.0.1:8000/api/redoc/)
