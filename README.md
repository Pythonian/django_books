~ $ mkvirtualenv books --python=/usr/bin/python3.9
(books) ~ $ git clone https://github.com/Pythonian/django_books.git
(books) ~ $ cd django_books
(books) ~/django_books (main)$ pip install -r requirements.txt
(books) ~/django_books (main)$ python manage.py collectstatic

Web tab > Source code
/home/africanliterature/django_books/ 

Web tab > virtualenv
/home/africanliterature/.virtualenvs/books/

/media/ - /home/africanliterature/django_books/media/
/static/ - /home/africanliterature/django_books/static/

import os
import sys

path = '/home/africanliterature/django_books'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_books.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Graph Models

Install requirements: pip install django-extensions pyparsing pydot pydotplus

Add 'django_extensions', to installed apps

Add the needed apps for the graphs in settings

    GRAPH_MODELS = {
        'app_labels': ["medicine", "account"],
    }

Create the graph models with the command
    
    python manage.py graph_models --pydot -a -g -o django_books.png
    python manage.py graph_models -a --arrow-shape normal -o django_books.png
