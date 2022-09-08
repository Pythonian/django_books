# African books

A web based application which enables users to download literary works from African authors, allow users of the platform to request for unavailable books and also give them an opportunity to share their own stories.

## Quick setup

1. Open your command line and clone the repo
```sh
git clone https://github.com/Pythonian/django_books.git
```

2. Change into project directory
```sh
cd django_books
```

3. Install project requirements
```sh
pip install -r requirements.txt
```

4. Run the migrations
```sh
python manage.py migrate
```

5. Load the database fixtures
```sh
python manage.py loaddata data.json
```

6. Create a superuser
```sh
python manage.py createsuperuser
```

7. Start the development server
```sh
python manage.py runserver
```

8. Visit the web app in your browser
```sh
localhost:8000
```

9. Likewise access the admin with the credentials you created in step 6
```sh
localhost:8000/admin
```