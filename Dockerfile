# base image  
FROM python:3.10 
USER root 

WORKDIR /home/app

# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

ARG DJANGO_SECRET_KEY
ARG DSN_SENTRY
ARG DEBUG

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DSN_SENTRY=$DSN_SENTRY
ENV DEBUG=$DEBUG


# set work directory
# RUN \
    # mkdir -p $DockerHOME && \
    # mkdir -p $DockerHOME/web/staticfiles

# where your code lives
COPY ./requirements.txt .
# install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .

USER root  

RUN python manage.py collectstatic --no-input
# start server  
# CMD python manage.py runserver 0.0.0.0:$PORT
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
