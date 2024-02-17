# How to run project with Redis and Celery 

1. Run Redis in docker by command - `sudo docker run -d -p 6379:6379 redis`
2. Run Celery locally by command - `celery -A apps.main worker -l INFO`
3. Run test by command - `python manage.py test apps`
4. Run the Django project and I'll start praying that this crap works well 🙏