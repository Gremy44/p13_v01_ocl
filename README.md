## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Deploiement

#### Stack utilisée :
- Django 
- Github
- Circle CI 
- Docker
- Heroku
- Sentry

> Pour le CI/CD à chaque push sur la branch main de Github, Circleci effectue ses tests et crée une image Docker du projet qu'il poussera sur Heroku.


## Parametrer la stack pour le déploiement
### Docker

Pour utiliser Docker : 
- Créez vous un compte sur le site de docker pour pouvoir utiliser le dockerHub
- Téléchargez et installez l'application DockerDesktop
Le projet à un fichier Dockerfile qui construit une image simple de notre application. C'est l'image créé par notre fichier Dockerfile qu'on va utilisée pour le deploiement.

Pour créer votre image docker suivez les étapes suivantes : 
- Veillez à bien avoir installer les dépendances du projet avec : `pip install -r requirements.txt`
- Installer DockerDesktop à partir du site de Docker : `https://www.docker.com/products/docker-desktop/`
- Une fois DockerDesktop démarrer sur votre machine, créer votre image avec la commande suivante : `docker build -t <nom-de-votre-image>:<version-de-votre-image> .`
- Ensuite, démarrez votre image Docker avec cette commande : `docker run -p 8000:8000 --env-file .env <nom-de-votre-image>`
- Vous pourrez accéder à votre image à l'URL suivante : `localhost:8000` ou `127.0.0.1:8000`

### Journalisation avec Sentry

Sentry va nous servir popur la journalisation et le suivi de notre application. Pour l'utiliser :
- allez sur le site de `sentry.io`
- créer vous un compte 
- créer un nouveau projet à partir de votre dashboard qu'on va ensuite lier à notre projet
- générez votre clef DSN
- dans votre projet installer la librairie de sentry
- Ajouter votre clef DSN avec le nom DSN_SENTRY dans votre fichier .env

### Deploiement sur Heroku

- Pour utiliser les services de Heroku vous devrez créer un compte.
- Une fois fait, rendez-vous sur votre page personnelle pour créer une nouvelle app en cliquant sur le bouton **new**.
- Renseigner les champs qui vous sont demandés.
- Rendez-vous ensuite dans les settings de votre application pour y entrer les variables d'environnement de votre application. Ici vous devrait entrer les variables : 
  + DJANGO_SECRET_KEY
  + DSN_SENTRY
  + DEBUG
- Vérifier que votre nom d'application est correcte.

### Circle CI
Pour faire fonctionner tout le pipeline de deploiement continue, nous utiliserons l'app wep de Circleci. Pour l'utiliser vous devrez créer un compte sur le site de Circleci, lier votre repo Github et parametrer les variables d'environnement de l'application

Variables d'environnement :
| NOM DE LA VARIABLE | VALEUR |
|:-------------------:|:-------|
|DJANGO_SECRET_KEY | Votre clef secrète Django
|DSN_SENTRY| Votre Dsn Sentry
|DEBUG|Valeur 0 ou 1 pour la production ou le developpement
|DOCKER_HUB_USERNAME| Votre nom d'utilisateur Docker
|DOCKER_HUB_PASSWORD| Votre mot de passe Docker
|IMAGE_NAME| Le nom de votre image Docker
|HEROKU_API_KEY| Votre clef API Heroku
|HEROKU_APP_NAME| Le nom de votre application sur Heroku

Une fois fait nous allons parametrer Heroku pour deployer notre application.
