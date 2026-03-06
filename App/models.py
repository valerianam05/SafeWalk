from pydantic import BaseModel,Field
from typing import Optional

class SafeZone(BaseModel):
    id: int
    nom: str
    latitude: float = Field(..., ge=-90, le=90, description="Latitude entre -90 et 90")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude entre -180 et 180")
    quartier: str
    is_open: bool = True 


class DangerReport(BaseModel):
    id: int
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    description: Optional[str] = None
    horodatage: str 