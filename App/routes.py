from fastapi import APIRouter
from models import SafeZone 
from models import  DangerReport
from database import load_data, save_data
from database import load_data, save_data, load_dangers, save_dangers
from database import load_data, calculate_distance 


router = APIRouter()

@router.get("/zones")
def get_all_zones():
    return load_data()

@router.post("/zones")
def create_zone(zone: SafeZone):
    zones = load_data()
    
    if any(z['id'] == zone.id for z in zones):
        raise HTTPException(status_code=400, detail="Cette zone existe déjà (ID doublon)")
    
    zones.append(zone.dict())
    save_data(zones)
    return {"status": "success", "message": "Zone enregistrée sur le disque !"}


# 1. Ta fonction de recherche améliorée (Nom OU Quartier)
@router.get("/zones/search")
def search_zones(query: str):
    zones = load_data()
    # On cherche si la requête est dans le nom OU dans le quartier
    results = [
        z for z in zones 
        if query.lower() in z['nom'].lower() or query.lower() in z['quartier'].lower()
    ]
    return results

@router.delete("/zones/{zone_id}")
def delete_zone(zone_id: int):
    zones = load_data()
    new_zones = [z for z in zones if z['id'] != zone_id]
    
    if len(new_zones) == len(zones):
        raise HTTPException(status_code=404, detail="Zone non trouvée")
        
    save_data(new_zones)
    return {"status": "success", "message": f"Zone {zone_id} supprimée"}


@router.get("/dangers")
def get_all_dangers():
    return load_dangers()  
@router.post("/dangers")
def report_danger(danger: DangerReport):
    dangers = load_dangers() 
    dangers.append(danger.dict())
    save_dangers(dangers)   
    return {"status": "success", "message": "Alerte de danger enregistrée !"}



@router.get("/zones/closest")
def get_closest_zone(user_lat: float, user_lon: float):
    zones = load_data()
    if not zones:
        raise HTTPException(status_code=404, detail="Aucune zone enregistrée")

    closest = min(
        zones, 
        key=lambda z: calculate_distance(user_lat, user_lon, z['latitude'], z['longitude'])
    )
    
    distance = calculate_distance(user_lat, user_lon, closest['latitude'], closest['longitude'])
    closest["distance_km"] = round(distance, 2)
    
    return closest