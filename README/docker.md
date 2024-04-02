### Запуск проекта:
- Создаем файл .env в корне проекта c параметрами указанными в .env.example:
    - nano .env

- Заменить настройки PostgreSQL на SQLite в файле settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'foodgram_db'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'collected_static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- Выполняем запуск:
    - docker compose -f docker-compose.yml up -d

- Делаем миграции и наполняем БД.
    - docker container exec -it TastyLink_backend sh -c "python manage.py migrate && python manage.py loaddb && python manage.py collectstatic && cp -r /app/collected_static/. /backend_static/static/"

### Пример запросов:
- [Главная страница: http://localhost:8000/](http://localhost:8000/)
- [Страница аутентификации: http://localhost:8000/signin](http://localhost:8000/signin)
- [Страница рецептов: http://localhost:8000/recipes](http://localhost:8000/recipes)
- [Страница подписок: http://localhost:8000/subscriptions](http://localhost:8000/subscriptions)
- [Страница создания рецепта: http://localhost:8000/recipes/create](http://localhost:8000/recipes/create)
- [Страница избранных рецептов: http://localhost:8000/favorites](http://localhost:8000/favorites)
- [Страница списка покупок: http://localhost:8000/cart](http://localhost:8000/cart)