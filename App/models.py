from pydantic import BaseModel

class SafeZone(BaseModel):
    id: int
    nom: str
    latitude: float
    longitude: float