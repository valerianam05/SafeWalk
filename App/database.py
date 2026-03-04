import json
import os

FILE_PATH = "data/zones.json"

def load_data():
    """Charge les zones depuis le fichier JSON."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_data(zones):
    """Sauvegarde la liste des zones dans le fichier JSON."""
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(zones, f, indent=4, ensure_ascii=False)