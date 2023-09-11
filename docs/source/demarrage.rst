*************************
Demarrage rapide en local
*************************

.. toctree::
    :maxdepth: 2

Prépartion de l'environnement
=============================

Ce guide vous explique les étapes pour créer et configurer l'environnement nécessaire à l'exécution du programme. Suivez ces instructions pour une mise en place rapide.

1. Création de l'Environnement Virtuel
--------------------------------------

Pour démarrer, suivez ces étapes :

1. Installer une version de Python compatible avec votre ordinateur. (https://www.python.org/downloads/)
2. Ouvrez le terminal (ou invite de commande) et placez-vous dans le dossier principal (dossier racine) du projet.

3. Tapez la commande suivante dans votre terminal pour créer un environnement virtuel nommé "venv" :

.. code-block:: bash

   python -m venv venv

Un répertoire appelé "venv" sera créé dans le dossier.

2. Activation de l'Environnement Virtuel
----------------------------------------

Pour activer l'environnement virtuel créé, suivez ces étapes :

1. Assurez-vous d'être dans le dossier principal (dossier racine) du projet avec le terminal.

2. Tapez la commande suivante pour activer l'environnement virtuel :

.. code-block:: bash

   venv\Scripts\activate

Cela ajoutera le préfixe "venv" à chaque ligne de commande dans votre terminal.

Pour désactiver l'environnement virtuel, utilisez cette commande :

.. code-block:: bash

   deactivate

4. Installation des Librairies
------------------------------

1. Assurez-vous d'être dans le dossier où se trouve le fichier "requirements.txt" avec l'environnement virtuel activé.

2. Pour installer les librairies requises, utilisez la commande suivante :

.. code-block:: bash

   pip install -r requirements.txt

Création des variables d'environnement
--------------------------------------

A la racine du projet, créer un fichier **.env** et ajouter les variables d'environnement suivantes :

.. code-block:: shell

    DJANGO_SECRET_KEY="votre_clef_secrete_Django"
    SENTRY_DSN="votre_DSN_Sentry"
    DEBUG="1_ou_0"

- **DJANGO_SECRET_KEY** est générer aléatoirement avec *get_random_secret_key*.
- **SENTRY_DSN :** doit être récupérée sur votre compte Sentry (se rendre à la section **installation** pour plus d'informations).
- **DEBUG :** doit être mis à 1 pour être en mode developpement ou 0 pour être en mode production.

5. Exécution de l'Application
-----------------------------

Utilisez ces étapes pour exécuter l'application :

1. Lancez le serveur :

   - Assurez-vous d'être dans le dossier principal du projet avec l'environnement virtuel activé.
   - Utilisez la commande suivante :

     .. code-block:: bash

        python manage.py runserver

2. Accédez à l'application dans le navigateur de votre choix :

   - Ouvrez votre navigateur web.
   - Rendez-vous à l'adresse : http://127.0.0.1:8000/

Commencez dès maintenant à utiliser l'application et à explorer ses fonctionnalités passionnantes !