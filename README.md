# SimpleDjangoProject
Russian readme: [there](README.ru.md)

Just a simple project on Django for my portfolio. 
The project consists of django application with several functions in it(many of them are useless, though).

## How to run the project
First of all, install required packages in python:
~~~
pip install -r requirements.txt
~~~
After that run it how you run other django-projects:
~~~
python manage.py runserver
~~~
## Building the docs
~~~
cd docs
sphinx make html
~~~
After building complete,there will be new directory *build*, where you can find the docs