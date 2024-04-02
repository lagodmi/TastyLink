### Запуск backend:

- Создаем файл .env в корне проекта c параметрами указанными в .env.example
- [Заменить настройки PostgreSQL на SQLite в файле settings](settings_sqlite.py)
- Выполняем запуск:
    - python manage.py migrate && python manage.py loaddb && python manage.py runserver
