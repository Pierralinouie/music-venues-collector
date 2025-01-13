import os
from dotenv import load_dotenv
from scrapers.venue_scraper import VenueScraper
from database.firebase_manager import FirebaseManager
from utils.logger import setup_logger

# Chargement des variables d'environnement
load_dotenv()

# Configuration du logger
logger = setup_logger()

def main():
    try:
        # Initialisation de Firebase
        firebase_manager = FirebaseManager(
            os.getenv('FIREBASE_CREDENTIALS_PATH')
        )
        
        # Initialisation du scraper
        scraper = VenueScraper(
            google_maps_api_key=os.getenv('GOOGLE_MAPS_API_KEY')
        )
        
        # Lancement de la collecte
        logger.info('Démarrage de la collecte')
        venues_data = scraper.collect_data()
        
        # Sauvegarde dans Firebase
        firebase_manager.save_venues(venues_data)
        logger.info('Collecte terminée avec succès')
        
    except Exception as e:
        logger.error(f'Erreur lors de la collecte : {str(e)}')

if __name__ == '__main__':
    main()