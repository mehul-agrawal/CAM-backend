web: python manage.py collectstatic --no-input; gunicorn core.wsgi --log-file - --log-level debug
release: python manage.py migrate