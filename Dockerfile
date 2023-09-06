# base image  
FROM python:3.10  
# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DockerHOME=/home/app 
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DEBUG $DEBUG
ENV DSN_SENTRY $DSN_SENTRY
ENV PORT 8000

# set work directory
RUN \
    mkdir -p $DockerHOME && \
    mkdir -p $DockerHOME/web/staticfiles

# where your code lives
WORKDIR $DockerHOME

# copy project
COPY . $DockerHOME

# install dependencies
RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# RUN python manage.py collectstatic --noinput

# start server  
CMD python manage.py runserver 0.0.0.0:$PORT
# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
