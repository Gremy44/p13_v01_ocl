# base image  
FROM python:3.10  
# setup environment variable  
ENV DockerHOME=/home/app 

# set work directory
RUN mkdir -p $DockerHOME
RUN mkdir -p $DockerHOME/web/staticfiles

# where your code lives
WORKDIR $DockerHOME

ARG DJANGO_SECRET_KEY
ARG DEBUG
ARG DSN_SENTRY

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $DockerHOME

# install dependencies
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --noinput

# start server  
CMD python manage.py runserver 0.0.0.0:$PORT
# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
