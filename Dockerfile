# base image  
FROM python:3.10 

# setup work directory
WORKDIR /home/app

# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_SECRET_KEY
ARG DEBUG
ARG DSN_SENTRY

# copy project
COPY . .

#install dependencies
RUN pip install -r requirements.txt --no-cache-dir 

# RUN python manage.py collectstatic --noinput

# start server  
CMD python manage.py runserver 0.0.0.0:$PORT

