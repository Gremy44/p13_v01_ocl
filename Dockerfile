# base image  
FROM python:3.10 

WORKDIR /home/app

# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_SECRET_KEY
ARG DSN_SENTRY
ARG DEBUG

COPY . .

RUN pip install -r requirements.txt --no-cache-dir 

# RUN python manage.py collectstatic --no-input
# start server  
# CMD python manage.py runserver 0.0.0.0:$PORT
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
