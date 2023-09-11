************
Introduction
************

.. toctree::
   :maxdepth: 2

Le projet
+++++++++

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers.

Amélioration de l'Architecture Modulaire
++++++++++++++++++++++++++++++++++++++++

La première partie du projet consiste à améliorer l'architecture de l'application en la rendant plus modulaire.
Pour cela, nous allons scinder l'application principale oc_lettings_site en 3 applications distinctes :
    - lettings.
    - profiles.
    - oc_lettings_site.

Mise en place d'un pipeline de déploiement CI/CD
++++++++++++++++++++++++++++++++++++++++++++++++

Une fois la structure de l'application bien séparée, nous allons mettre en place un pipeline de déploiement CI/CD.
Pour cela, nous allons utiliser les outils suivants :
    - CircleCI.
    - Docker.
    - Heroku.

.. note::
   Le fonctionnement sera le suivant : à chaque push sur la branche 'main', on va déclencher les tests et le déploiement automatiquement.
