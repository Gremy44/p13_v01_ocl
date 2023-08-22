FROM python:latest

WORKDIR /app

# set environnement variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_SECRET_KEY
ARG DSN_SENTRY
ARG DEBUG

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DSN_SENTRY=$DSN_SENTRY
ENV DEBUG=$DEBUG

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]