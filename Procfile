web: .heroku/venv/bin/gunicorn_django -b 0.0.0.0:$PORT -w 9 -k gevent --max-requests 250 --preload settings.prod
# web: gunicorn_django clubs.wsgi -b 0.0.0.0:$PORT
# web: python2.7 manage.py runserver 0.0.0.0:$PORT --noreload