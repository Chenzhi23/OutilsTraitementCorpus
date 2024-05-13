# Système de Classification Automatique de Contenus Vidéo YouTube

## Description du Projet (Tâche)
Ce projet vise à développer un système automatique de classification de textes basé sur les descriptions de vidéos YouTube. L'objectif est de catégoriser automatiquement les vidéos en fonction de leur contenu descriptif, ce qui aidera les utilisateurs à trouver plus rapidement les types de vidéos qui les intéressent, tout en aidant les créateurs de contenu et les annonceurs à mieux cibler leur audience.

## Jeu de Données
Les descriptions des vidéos seront récupérées via l'API YouTube Data, incluant le titre, la description, les tags, et d'autres métadonnées. Ces informations seront utilisées pour entraîner et tester le modèle de classification de texte.

- **Source des Données** : API YouTube Data
- **Taille des Données** : Environ 600 descriptions de vidéos issu de 600 vidéos de Youtube
- **Train-test split** :
  - **Train** : 420 descriptions (70%)
  - **Test** : 180 description (30%)
- **Champs des Données** :
  - **ID Vidéo** : Identifiant unique de la vidéo
  - **Titre** : Youtubeur
  - **Description** : Description détaillée du contenu de la vidéo
  - **Catégorie** : Catégorie attribuée manuellement en fonction du contenu de la vidéo


## Langue
Français

## Objectifs du Projet
Classer automatiquement les vidéos dans des catégories prédéfinies telles que « Actualité », « Cuisine », « Maquillage », etc., en se basant sur le texte de leur description.

## Conception du Modèle
- **Prétraitement** : Nettoyage des données textuelles, suppression des mots inutiles, ponctuation, normalisation du texte, etc.
- **Extraction de caractéristiques** : Transformation du texte en vecteurs numériques à l'aide de méthodes telles que TF-IDF ou Word2Vec ou Sac de mots.
- **Algorithmes de classification** : Expérimentation avec différents modèles d'apprentissage automatique tels que SVM (machines à vecteurs de support), forêts aléatoires, réseaux de neurones, etc.
- **Évaluation du modèle** : Utilisation de métriques telles que la précision, le rappel, et le score F1 pour évaluer la performance du modèle.

## Applications
- **Découverte de contenu** : Permettre aux utilisateurs de filtrer rapidement les vidéos par catégorie.
- **Recommandation de contenu** : Améliorer la précision des systèmes de recommandation en proposant des contenus plus adaptés aux intérêts des utilisateurs.
- **Ciblage publicitaire** : Aider les annonceurs à cibler plus précisément des types spécifiques de contenus vidéo, augmentant ainsi l'efficacité des campagnes publicitaires.

## Partage de Connaissances
À la fin du projet, le code source et les modèles pré-entraînés seront partagés sur GitHub, avec une documentation détaillée sur le processus de prétraitement des données, l'entraînement des modèles et l'évaluation des résultats.

