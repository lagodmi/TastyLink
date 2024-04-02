# "TastyLink" — ваш надежный помощник в мире кулинарии.

## Описание проекта:
"TastyLink" представляет собой веб-платформу с полным функционалом по авторизации, предоставляющую авторизованным пользователям возможность выкладывать свои уникальные рецепты, подписываться на других участников сообщества, добавлять понравившиеся рецепты в избранное и создавать персонализированные списки покупок.

Благодаря "TastyLink" вы сможете наслаждаться удобством и вдохновением, исследуя мир вкусных блюд и деликатесов, а также делиться своими кулинарными шедеврами с другими любителями гастрономии.

## Стек проекта:
- Python 3.9
- Django 3.2.3
- Django REST framework 3.12.4
- JavaScript

## Процесс запуска проекта (через docker compose):
- Для разработки, тестирования или демонстрации концепции docker-compose.yml.
### Запуск проекта:
- [Клонируем репозиторий](https://github.com/lagodmi/foodgram-project-react.git)
- Создаем файл .env в корне проекта c параметрами указанными в .env.example:
    - nano .env
- Выполняем запуск:
    - docker compose -f docker-compose.yml up -d
- Делаем миграции и наполняем БД.
    - docker container exec -it TastyLink_backend sh -c "python manage.py migrate && python manage.py loaddb && python manage.py collectstatic && cp -r /app/collected_static/. /backend_static/static/"
- [Проект доступен на: http://localhost:8000/](http://localhost:8000/)
### Пример запросов:
- [Страница аутентификации: http://localhost:8000/signin](http://localhost:8000/signin)
- [Страница рецептов: http://localhost:8000/recipes](http://localhost:8000/recipes)
- [Страница подписок: http://localhost:8000/subscriptions](http://localhost:8000/subscriptions)
- [Страница создания рецепта: http://localhost:8000/recipes/create](http://localhost:8000/recipes/create)
- [Страница избранных рецептов: http://localhost:8000/favorites](http://localhost:8000/favorites)
- [Страница списка покупок: http://localhost:8000/cart](http://localhost:8000/cart)
## Автор проекта:
Лагоднов Д.С.
