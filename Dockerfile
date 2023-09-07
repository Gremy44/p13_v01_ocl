# base image  
FROM python:3.10  
# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DockerHOME=/home/app
ENV PORT 8000
ARG DJANGO_SECRET_KEY
ARG DSN_SENTRY
ARG DEBUG


# set work directory
# RUN \
    # mkdir -p $DockerHOME && \
    # mkdir -p $DockerHOME/web/staticfiles

# where your code lives
WORKDIR $DockerHOME

# copy project
COPY . $DockerHOME

# install dependencies
RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir &&\
    python manage.py collectstatic --noinput

# start server  
CMD python manage.py runserver 0.0.0.0:$PORT
# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
