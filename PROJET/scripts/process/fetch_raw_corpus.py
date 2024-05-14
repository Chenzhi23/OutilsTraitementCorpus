from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv, re, emoji, argparse, os

def description_parser(channel_name: str, max_video_results: int, video_type: str) -> list:
    """
    Récupère les descriptions des vidéos d'une chaîne YouTube spécifique.

    Args:
        channel_name (str): Le nom de la chaîne YouTube dont on veut récupérer les descriptions des vidéos.
        max_video_results (int): Le nombre maximal de descriptions de vidéos à récupérer.
        video_type (str): Le type de vidéo, utilisé pour étiqueter les descriptions récupérées.

    Returns:
        list: Une liste de tuples, chaque tuple contenant la description d'une vidéo et son type.

    Raises:
        HttpError: Une erreur de l'API YouTube.
        KeyError: Une clé manquante dans la réponse de l'API.
    """
    
    # Votre clé API YouTube
    api_key = ''

    # Création d'un client API pour communiquer avec YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        # Recherche l'ID de la chaîne à partir de son nom
        search_response = youtube.search().list(
            part='snippet',
            q=channel_name,
            type='channel',
            maxResults=1
        ).execute()

        if 'items' in search_response and len(search_response['items']) > 0:
            channel_id = search_response['items'][0]['snippet']['channelId']

            # Obtient l'ID de la playlist des vidéos uploadées de la chaîne
            channel_response = youtube.channels().list(
                part='contentDetails',
                id=channel_id
            ).execute()

            uploads_list_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

            # Récupère les vidéos de la playlist et leurs descriptions
            playlist_response = youtube.playlistItems().list(
                part='snippet',
                playlistId=uploads_list_id,
                maxResults=max_video_results
            ).execute()

            video_descriptions = []
            for item in playlist_response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_response = youtube.videos().list(
                    part='snippet',
                    id=video_id
                ).execute()
                video_description = video_response['items'][0]['snippet']['description']
                if video_description:
                    # Nettoyage de la description
                    video_description = emoji.demojize(video_description, delimiters=('###', '###'))
                    video_description = re.sub(r'(###.*###)', '', video_description)
                    video_description = re.sub(r'\n', ' ', video_description)
                    video_description = re.sub(r'https?://\S+|www\.\S+', '', video_description)
                    video_description = re.sub(r'[^\w\s,.\']', '', video_description)
                    video_description = re.sub(r'\s{2,}', ' ', video_description).lower()
                    video_descriptions.append((video_description, video_type))

            return video_descriptions

        else:
            print("Aucune chaîne correspondante trouvée, veuillez vérifier le nom fourni.")

    except HttpError as e:
        print("Erreur de requête :", e)
    except KeyError as e:
        print("Clé manquante dans la réponse :", e)


def export_txt(video_descriptions: list, folder_path: str, start_number: int) -> None:
    """
    Exporte les descriptions de vidéos dans des fichiers texte.

    Args:
        video_descriptions (list): Une liste de tuples contenant les descriptions des vidéos et leur type.
        folder_path (str): Le chemin du dossier où les fichiers texte seront sauvegardés.
        start_number (int): Le numéro de départ pour la nomination des fichiers texte.

    Returns:
        None
    """
    for index, (description, _) in enumerate(video_descriptions, start=start_number):
        file_path = os.path.join(folder_path, f"t{index}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(description)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Récupère et sauvegarde les descriptions des vidéos YouTube d'une chaîne spécifique.")
    parser.add_argument("-y", "--youtuber_name", type=str, required=True, help="Le nom du YouTubeur dont on veut récupérer les descriptions des vidéos.")
    parser.add_argument("-m", "--max_results", type=int, required=True, help="Le nombre maximal de descriptions de vidéos à récupérer.")
    parser.add_argument("-t", "--tag", type=str, help="Le type de vidéo pour étiqueter les descriptions récupérées.")
    parser.add_argument("-o", "--output_folder", type=str, required=True, help="Le chemin du dossier où les fichiers texte seront sauvegardés.")
    parser.add_argument("-s", "--start_number", type=int, help="Le numéro initial pour nommer les fichiers texte.", default=1)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    video_descriptions = description_parser(args.youtuber_name, args.max_results, args.tag)
    if video_descriptions:
        export_txt(video_descriptions, args.output_folder, args.start_number)
