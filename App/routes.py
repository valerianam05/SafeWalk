from fastapi import APIRouter
from models import SafeZone 

router = APIRouter()
base_de_donnees = [] 

@router.get("/zones")
def lire_zones():
    return base_de_donnees

@router.post("/zones")
def ajouter_zone(zone: SafeZone):
    base_de_donnees.append(zone)
    return {"message": "Zone ajoutée !", "data": zone}