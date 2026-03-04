from pydantic import BaseModel

class SafeZone(BaseModel):
    id: int
    nom: str
    latitude: float
    longitude: float


class DangerReport(BaseModel):
    id: int
    type_danger: str  
    description: str
    quartier: str
    heure_signalement: str 