# SafeWalk API

Ce projet est une API de sécurité urbaine développée avec **FastAPI**. 
Mon objectif principal était d'apprendre à construire une API en Python, en gérant la persistance des données et la logique géographique.

## Objectifs d'apprentissage
- Création de routes API (GET, POST, DELETE) avec **FastAPI**.
- Validation de données avec **Pydantic**.
- Gestion de la persistance des données via des fichiers **JSON** (sans base de données SQL pour rester léger).
- Implémentation d'algorithmes mathématiques (Formule de **Haversine**) pour le calcul de distance GPS.

## Fonctionnalités
- **Gestion des Zones Sûres** : Ajouter, lister et supprimer des lieux sécurisés à Antananarivo.
- **Signalement de Danger** : Système d'alertes communautaires pour signaler des incidents en temps réel.
- **Recherche de Proximité** : Calcul automatique de la zone de sécurité la plus proche de l'utilisateur.

