***Installation Step***
python -m venv venv
pip install django djangorestframework requests

***Required dependencies and versions***
python==3.8
Django==4.2
djangorestframework==3.14

***Database setup and configuration***
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 ***Running the application***
 python3 manage.py createsuperuser
 python manage.py runserver
