---
licence: MIT
langue: Français
taille: "1 GB"
balises:
  - classification de texte
  - apprentissage automatique
  - vidéos YouTube
configuration:
  format_fichier: csv
  partage:
    entrainement: 70%
    test: 30%
---

## Exemple de données

| ID | Description | Catégorie |
|----|-------------|----------|
| 1  | dans les pyrénéesorientales, un nouveau départ de feu a ravagé 3 hectares et menacé plusieurs habitations avant dêtre fixé. toute lactualité en direct sur suiveznous sur les réseaux instagram facebook tiktok twitter | actualite |
| 2  | le pire vs le meilleur mais... nouveau concept avec hugoposé et nico je teste le nouveau mcdo une arnaque activez la cloche de notification, pour être au courant de mes vidéos mes restaurants pepe chicken twitter fastgoodcuisine instagram fastgoodcuisine snapchat fastgoodcuisine facebook fastgoodcuisine merci à mathias pour la coupe de cheveux insta barber_factory 16 rue jules vallès, 75011 paris sponsorship contactfastgoodcuisine.com | cuisine |
| 3  | rejoins moi tik tok le monde de salome instagram lemondedesalome contact professionnel uniquement lemondedesalomeytgmail.com vu dans la video je porte pull pimkie ancienne co jean claudie pierlot ancienne co montre apple watch se 40mm lunettes caroline abraam materiel video materiel video camera trepieds logiciel de montage final cut pro miniatures photoshop musiques epidemicsounds musique doutro faller ikhana collaboration commerciale produit recu gratuitement lien daffiliation je touche une petite commission si vous achetez via ce lien cette video nest pas en collaboration remuneree. | maquillage |

# Système de Classification Automatique de Contenus Vidéo YouTube

## Description du Projet (Tâche)
Ce projet vise à développer un système automatique de classification de textes basé sur les descriptions de vidéos YouTube. L'objectif est de catégoriser automatiquement les vidéos en fonction de leur contenu descriptif. Ce système aidera les utilisateurs à trouver plus rapidement les types de vidéos qui les intéressent, tout en permettant aux créateurs de contenu et aux annonceurs de mieux cibler leur audience.

## Jeu de Données

### Description
Les descriptions des vidéos sont extraites en utilisant l'API YouTube Data. Chaque enregistrement contient le titre, la description complète, les tags et d'autres métadonnées pertinentes. Ces informations sont cruciales pour entraîner et évaluer le modèle de classification.

### Source des Données
- **Source Principale** : API YouTube Data
- **Nombre de Vidéos** : 600 vidéos YouTube
- **Répartition Train-Test** :
  - **Entraînement** : 420 descriptions (70%)
  - **Test** : 180 descriptions (30%)

### Champs des Données
- **ID Vidéo** (`video_id`): Identifiant unique de la vidéo.
- **Titre** (`title`): Le titre de la vidéo.
- **Description** (`description`): Description textuelle détaillée du contenu de la vidéo.
- **Catégorie** (`category`): Catégorie attribuée manuellement basée sur le contenu de la vidéo.

## Langue du Jeu de Données
Toutes les descriptions sont en **Français**.

## Objectifs du Projet
L'objectif principal est de classifier automatiquement les vidéos dans des catégories prédéfinies telles que « Actualité », « Cuisine », « Maquillage », en utilisant le texte de leur description.

## Conception du Modèle

### Prétraitement des Données
- **Nettoyage Textuel** : Élimination des stop words, des mots peu fréquents, de la ponctuation.
- **Normalisation** : Conversion du texte en minuscules, suppression des accents et des caractères spéciaux.

### Extraction de Caractéristiques
- **TF-IDF** : Utilisation de l'approche Term Frequency-Inverse Document Frequency pour convertir le texte en un vecteur numérique.
- **Sac de Mots** : Transformation des descriptions en vecteurs de fréquence de mots.

### Modèles de Classification
- **SVM (Support Vector Machines)**
- **Forêts Aléatoires (Random Forests)**
- **Réseaux de Neurones (Neural Networks)**

### Évaluation du Modèle
- **Métriques** : Précision (Precision), Rappel (Recall) et Score F1 pour évaluer les performances du modèle sur le jeu de données de test.

## Applications du Projet

### Découverte de Contenu
Aider les utilisateurs à naviguer et à filtrer les vidéos par catégories de manière efficace.

### Recommandation de Contenu
Améliorer la pertinence des recommandations de vidéos en utilisant les catégories prédites pour matcher les préférences des utilisateurs.

### Ciblage Publicitaire
Optimiser les campagnes publicitaires en ciblant les vidéos qui correspondent le mieux au public visé.

## Partage de Connaissances
Le code source et les modèles entraînés seront disponibles sur GitHub pour la communauté. Une documentation complète expliquera le processus de prétraitement, d'entraînement des modèles, et d'évaluation des performances, pour encourager la réutilisation et la collaboration.

## Information sur la Maintenance du Jeu de Données
- **Mainteneur** : Chenzhi Sun (Étudiant du pluriTAL)
- **Contact** : chenzhisun23.gmail.com
- **Fréquence de Mise à Jour** : Le jeu de données est prévu pour être mis à jour annuellement pour inclure les articles les plus récents.