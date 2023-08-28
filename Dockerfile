# base image  
FROM python:3.8   
# setup environment variable  
ENV DockerHOME=/home/app 
#/webapp


# set work directory
RUN mkdir -p $DockerHOME

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

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
