import os
import re
import emoji
import argparse

def clean_text(text):
    """
    Nettoie le texte en éliminant les emojis, les URLs, les caractères spéciaux et les espaces superflus.

    Paramètres :
    text (str): Le texte original à nettoyer.

    Retourne :
    str: Le texte nettoyé.
    """
    # Supprimer les emojis
    text = emoji.demojize(text)
    text = re.sub(r':[a-zA-Z_]+:', '', text)

    # Supprimer les URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Supprimer les caractères spéciaux et réduire les espaces multiples
    text = re.sub(r'[^\w\s,.\']', '', text)
    text = re.sub(r'\s{2,}', ' ', text).strip()

    return text

def clean_files(input_folder, output_folder):
    """
    Lit et nettoie le contenu de tous les fichiers texte du dossier spécifié,
    puis enregistre les fichiers nettoyés dans le dossier de sortie spécifié.

    Paramètres :
    input_folder (str): Le chemin du dossier contenant les fichiers texte à nettoyer.
    output_folder (str): Le chemin du dossier où les fichiers nettoyés seront enregistrés.
    """
    # Vérifier si le dossier de sortie existe, sinon le créer
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                original_text = file.read()
            
            cleaned_text = clean_text(original_text)

            # Créer le chemin pour le fichier nettoyé dans le dossier de sortie
            clean_file_path = os.path.join(output_folder, filename)
            with open(clean_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)
            print(f'Le fichier {filename} a été nettoyé et enregistré sous {clean_file_path}.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nettoie les fichiers texte en supprimant les emojis, les URLs et les caractères spéciaux.")
    parser.add_argument("-i", "--input_directory", type=str, required=True, help="Le chemin du dossier contenant les fichiers texte à nettoyer.")
    parser.add_argument("-o", "--output_directory", type=str, required=True, help="Le chemin du dossier où les fichiers nettoyés seront sauvegardés.")
    args = parser.parse_args()

    # Exécuter la fonction de nettoyage
    clean_files(args.input_directory, args.output_directory)
