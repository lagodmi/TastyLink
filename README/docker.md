### Запуск проекта:
- Создаем файл .env в корне проекта c параметрами указанными в .env.example:
    - nano .env
- Выполняем запуск:
    - docker compose -f docker-compose.yml up -d
- Делаем миграции и наполняем БД.
    - docker container exec -it TastyLink_backend sh -c "python manage.py migrate && python manage.py loaddb && python manage.py collectstatic && cp -r /app/collected_static/. /backend_static/static/"