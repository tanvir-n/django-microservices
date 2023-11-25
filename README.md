# Instructions to run this repository
python -m venv msr

msr/Scripts/activate

pip install django, djangorestframework, django-cors-headers, requests

django-admin startproject mservice

django-admin startapp service1

django-admin startapp service2

python manage.py runserver

after creating model in service1 run the following command
python manage.py makemigrations
python manage.py migrate --database service1