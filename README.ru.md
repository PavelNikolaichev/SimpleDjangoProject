# SimpleDjangoProject
Документация на английском: [ТЫК](README.md).

Это довольно простой проект на джанго для моего портфолио.
Он состоит из веб-приложения, внутри которого есть куча разных функций(полезных и не очень).

## Начало работы
Выполните установку пакетов для python:
~~~
pip install -r requirements.txt
~~~
После этого запускаете его как и любое друое django-приложение:
~~~
python manage.py runserver
~~~
## Сборка документации
~~~
cd docs
sphinx make html
~~~
После этого создастся новая папка *build*, где находится собраная документация проекта.