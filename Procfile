release: python manage.py migrate
# chatworker: python manage.py runworker --settings=apexindustry.settings -v2

# web: daphne apexindustry.asgi:application
# chatworker: python manage.py runworker --settings=apexindustry.settings -v2
# celery -A apexindustry beat -l info
# web: gunicorn apexindustry.wsgi

web: daphne apexindustry.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A apexindustry.celery worker -1 info
celerybeat: celery -A apexindustry beat -1 INFO
celeryworker2: celery -A apexindustry.celery worker & celery -A apexindustry.celery worker -1 INFO & wait -n