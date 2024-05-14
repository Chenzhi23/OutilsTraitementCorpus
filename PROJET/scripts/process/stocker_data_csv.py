import os
import pandas as pd

def txt_to_csv(input_folder: str, output_csv: str, youtubers: list):
    """
    Lit des fichiers texte dans un dossier spécifié et enregistre leurs contenus dans un fichier CSV avec des informations supplémentaires.

    Paramètres :
        input_folder (str) : Le chemin vers le dossier contenant les fichiers texte.
        output_csv (str) : Le chemin où le fichier CSV sera enregistré.
        youtubers (list) : Liste des noms des chaînes YouTube. Chaque chaîne est assignée à 20 fichiers.

    Description :
        Cette fonction parcourt tous les sous-dossiers du dossier spécifié, lit les fichiers texte, et assemble les informations
        telles que le contenu du fichier, l'identifiant du fichier, la catégorie du fichier, et le nom de la chaîne YouTube correspondante
        dans un DataFrame. Le DataFrame est ensuite enregistré en tant que fichier CSV. Chaque nom de chaîne YouTube dans la liste
        est assigné à 20 fichiers de manière cyclique.
        
    Retour :
        None
    """
    data = []  # Initialisation de la liste de données

    # Obtenir tous les sous-dossiers
    categories = [f.name for f in os.scandir(input_folder) if f.is_dir()]
    categories.sort()  # Trier les catégories pour une consistance

    # Initialisation des variables pour l'assignation des Youtubers
    youtuber_index = 0
    file_count = 0  # Compteur de fichiers pour gérer l'assignation des Youtubers

    # Parcourir chaque catégorie
    for category in categories:
        category_folder = os.path.join(input_folder, category)
        files = sorted(os.listdir(category_folder))  # Trier les fichiers

        # Parcourir chaque fichier texte
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(category_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Création de l'ID du texte
                txt_id = f"{category[0]}{int(filename[1:-4])}"

                # Ajout des informations dans la liste de données
                data.append({
                    "ID txt": txt_id,
                    "Description": content,
                    "Catégorie": category,
                    "Youtuber": youtubers[youtuber_index]
                })

                # Mise à jour du compteur de fichiers et passage au Youtuber suivant si nécessaire
                file_count += 1
                if file_count == 20:
                    file_count = 0
                    youtuber_index = (youtuber_index + 1) % len(youtubers)

    # Création du DataFrame et enregistrement en tant que CSV
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False, sep=';')

# Paramètres du script
input_folder = '../../data/clean'
output_csv = '../../data/data.csv'
youtubers = ['HugoDécrypte - Actus du jour', 'TF1 INFO', 'franceinfo', 'RTL', 'BFMTV', 'Deli Cuisine', 'Hervé Cuisine', 'Norbert Tarayre', 'Cooking With Morgane', 'sandra-cuisine87', 'Dame Mature', 'Sananas', "It's Charlotte's Time", 'Beauty garden', 'Le monde de Salomé']

# Exécution de la fonction
txt_to_csv(input_folder, output_csv, youtubers)
