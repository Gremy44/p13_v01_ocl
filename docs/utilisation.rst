****************************
Utilisation pour deploiement
****************************

.. toctree::
   :maxdepth: 2

Introduction
++++++++++++

.. |github-logo| image:: _static/github.svg
   :alt: GitHub Logo
   :width: 20px

.. |github-actions-logo| image:: _static/githubactions.svg
   :alt: GitHub Actions Logo
   :width: 20px

.. |sentry-logo| image:: _static/sentry.svg
   :alt: Sentry Logo
   :width: 20px

.. |docker-logo| image:: _static/docker.svg
   :alt: Docker Logo
   :width: 20px

.. |django-logo| image:: _static/django.svg
   :alt: Django Logo
   :width: 20px

Vous trouverez ici les différentes étapes pour configurer l'application et les services tiers pour faire fonctionner correctement le projet en vue de le déployer.

.. warning::
    Pour que les étapes de ce chapitre fonctionnent, vous devez au préalable avoir exécuté les étapes du chapitre : **demarrage**.


Utilisation de Docker |docker-logo|
===================================

1. Installation  de Docker
--------------------------

Pour utiliser Docker Hub, il est nécessaire de créer un compte et d'installer Docker sur son ordinateur: `Docker <https://www.docker.com/>`_

Une fois le compte créé et docker installer sur votre ordinateur, vous pourrez envoyer des images sur votre dépôt Docker Hub

Créer un dépôt et donner lui le nom que vous souhaitez.

.. note::
    Le dépôt créé doit être public.

Pour push une image sur votre dépôt Docker, vous devez utiliser un fichier *Dockerfile*, comme celui-ci présent dans le projet.
Vous pouvez en créer un ou utiliser celui existant et le modifier selon vos besoins.

.. code-block:: docker

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

    EXPOSE 8000
    # start server  

    CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "oc_lettings_site.wsgi"]

2. Création et push de l'image vers votre dépôt Docker
------------------------------------------------------

.. code-block:: bash

    # Construction de l'image
    docker build -t ocl-docker:latest .

.. code-block:: bash

    # Push de l'image sur votre dépôt Docker
    docker push <votre_repo_docker>/ocl-docker:latest


.. note::
    Remplacer <votre_repo_docker> par le 'Namespace' et le 'repository name' choisis sur Docker Hub


3. Tester le fonctionnement de l'image
--------------------------------------

Pour lancer l'image créée localement exécuter les étapes suivantes.

.. important::
    Si vous utilisez *Docker Desktop* n'oubliez pas de le lancer avant.

.. code-block:: bash

    # Connexion à Docker
    docker login

.. code-block:: bash

    # Lancement de l'image en local
    docker run -it -p 8080:8080 <votre_repo_docker>/ocl-docker:latest

- Si vous souhaitez naviguer dans le projet pour vérifier des dossiers ou des fichiers.
  
.. code-block:: bash
 
    docker run -it <votre_repo_docker>/ocl-docker /bin/sh


Gestion est création des utilisateurs avec Django |django-logo|
===============================================================

1. Administration des utilisateurs
----------------------------------

Pour créer et gérer des utilisateurs, cela peut être fait de plusieurs manières par le shell Django ou par l'interface d'administration de Django.
Qui est accessible à l'adresse. (http://127.0.0.1:8000/admin/)

.. note::
    - nom d'utilisateur : admin
    - mots de passe : Abc1234!

Une fois connecter, vous pourrez administrer les utilisateurs et les objets *Lettings* et *Addresses*.

Utilisation de Sentry |sentry-logo|
===================================

1. Configuration de Sentry
--------------------------

Pour utiliser Sentry et pouvoir utiliser le monitoring sur le projet accédé à votre compte.

1. Créer un nouveau projet
2. Choisissez une plateforme pour le projet, dans notre cas Django.
3. Choisissez une équipe pour votre projet ensuite cliquer sur : **Créer un projet**
4. Une fois le projet créé, vous pourrez récupérer la clé **SENTRY_DSN** à intégrer dans le fichier **.env**

Une fois toutes ces étapes exécutées et le serveur local lancer, vous pourrez visualiser sur Sentry l'activité de l'application.

Sentry a été parametrer manuellement pour remonter plusieurs sorte d'informations : 
    - La route des utilisateurs : label : **info**
    - Les erreurs 404 : label : **warning**
    - Les erreurs 500 : label : **error**

.. important::
    Dans l'application 'oc_lettings_site' se trouve un fichier **logger.py**, c'est un décorateur qui est placé sur chaque vue pour journaliser les parcour utilisateur sur le site.

.. note::
    Pour que Sentry fonctionne correctement, il faut que le fichier **.env** soit correctement configuré.

Utilisation de Circleci
=======================

Pour utiliser l'outil d'intégration continue Circle ci

Circleci est un service d'intégration continue (CI) et de déploiement continu (CD). Il vous permet d'automatiser diverses tâches liées à votre projet, telles que les tests, les déploiements et plus encore. Dans ce chapitre, nous allons expliquer comment configurer et utiliser Circleci pour améliorer votre flux de travail de développement.

Configuration de Circleci
-------------------------

Pour que le workflow de Circleci fonctionne il vous faudra vous rendre dans l'appli web Circleci. Connectez votre compte Github à Circleci et choisissez le repo de projet. 
Dans **project setting**, créez les variables d'environnements une à une.

.. important::
    Il faudra créer les secrets suivants :

    - DJANGO_SECRET_KEY
    - DOCKER_HUB_PASSWORD
    - DOCKER_HUB_USERNAME
    - HEROKU_API_KEY
    - HEROKU_APP_NAME
    - SENTRY_DSN
    - IMAGE_NAME
    - DEBUG

- Fichier de configuration yaml pour Circleci qui déclenche le workflow à chaque `push` ou `pull request` sur la branche main :

.. code-block:: yaml

    version: 2.1 

    orbs:
    docker: circleci/docker@2.1.3
    python: circleci/python@2.0.3
    heroku: circleci/heroku@2.0.0

    jobs:
    run-test:
        docker:
        - image: cimg/python:3.10.2
        steps:
        - checkout
        - python/install-packages:
            pkg-manager: pip
            pip-dependency-file: requirements.txt
        - run:
            name: Run tests
            command: pytest

    build-push-docker:
        docker:
        - image: cimg/python:3.10.2
        steps:
        - checkout
        - setup_remote_docker
        - run:
            name: Build docker image
            command:
                docker build -t $IMAGE_NAME:$CIRCLE_SHA1 .
        - run:
            name: Connect to Docker Hub
            command:
                echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin
        - run:
            name: Push docker image
            command:
                docker tag $IMAGE_NAME:$CIRCLE_SHA1 $DOCKER_HUB_USERNAME/$IMAGE_NAME:$CIRCLE_SHA1 |
                docker push $DOCKER_HUB_USERNAME/$IMAGE_NAME:$CIRCLE_SHA1

    deploye-from-dockerhub-to-heroku:
        docker:
        - image: $DOCKER_HUB_USERNAME/$IMAGE_NAME:$CIRCLE_SHA1
        steps:
        - checkout
        - run:
            name: Deploy Main to Heroku
            command: |
                git push https://heroku:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git main


    workflows:
    version: 2
    run_tests_and_build_docker:
        jobs:
        - run-test
        - build-push-docker:
            filters:
                branches:
                only: main
            requires:
                - run-test
        - deploye-from-dockerhub-to-heroku:
            filters:
                branches:
                only: main
            requires:
                - build-push-docker

.. important::
    Le fichier doit être nommé **config.yml** et placé dans un repertoire nommé **.circleci** à la racine du projet. 

Utilisation de Heroku
=====================

Suivez les étapes suivantes pour mettre en place le déploiement continu sur Heroku :
    - Pour utiliser les services de Heroku vous devrez créer un compte.
    - Une fois fait, rendez-vous sur votre page personnelle pour créer une nouvelle app en cliquant sur le bouton **new**.
    - Renseigner les champs qui vous sont demandés.
    - Rendez-vous ensuite dans les settings de votre application pour y entrer les variables d'environnement de votre application. Ici vous devrait entrer les variables : 
        + DJANGO_SECRET_KEY
        + DSN_SENTRY
        + DEBUG
    - Vérifier que votre nom d'application est correcte.

.. note::
    le deploiement sur Heroku est géré avec le fichier **`heroku.yml`** à la racine du projet

.. important::
    Si vous avez fait des modifications sur les fichiers statics et que ceux-ci vous conviennent, n'oubliez pas d'executer la commande suivante pour les collecter : 
    .. code-block:: bash

        python manage.py collectstatic --noinput