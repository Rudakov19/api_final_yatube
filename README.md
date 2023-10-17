# API для социальной сети блогеров Yatube
### Описание:
Проект построен на Django и Django Rest Framework.
Проект позволяет просматривать и публиковать авторские статьи по категориям.
Происходит авторизация пользователей.
Авторизованный пользователь может публиковать посты и оставлять комментарии к постам других авторов, а также подписываться на них.
### Технологии:
- Django==3.2.16
- pytest==6.2.4
- pytest-pythonpath==0.7.3
- pytest-django==4.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Rudakov19/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры запросов и ответов:
#### Запрос:
| Ресурс | Тип | Путь |
| ------ | ------ | ------ |
| Получить список постов | GET | /api/v1/posts/ |
#### Ответ:
```
count: 123
next: http://api.example.org/accounts/?offset=400&limit=100
previous: http://api.example.org/accounts/?offset=200&limit=100
results:
  -
    id: 0
    author: string
    text: string
    pub_date: 2021-10-14T20:41:29.648Z
    image: string
    group: 0
```
### Автор:
_[Дмитрий Рудаков](https://github.com/Rudakov19)_
