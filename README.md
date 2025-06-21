# basketball-players

### comandos
```
python -m venv venv
source venv/bin/activate
```

```
pip install django djangorestframework drf-yasg djangorestframework-simplejwt
django-admin startproject nba_project
cd nba_project
python manage.py startapp nba
```



```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py createsuperuser
```

```
python manage.py loaddata nba_fixtures.json
```

```
python manage.py runserver
```

```
npx create-react-app nba-frontend
cd nba-frontend
npm install axios react-router-dom
```