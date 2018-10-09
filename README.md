**Зависимости - python 3, django 2, django-rest-framework**

pip3 install django djangorestframework



**Инструкция по развертыванию**

git clone git@github.com:kotlyar562/test-task.git
cd test-task
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
create countries in admin interface http://localhost:8000/admin/
watch result http://localhost:8000
