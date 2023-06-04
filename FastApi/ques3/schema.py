from pydantic import BaseModel

class coordinateRequest(BaseModel):
    lat1 : float
    long1 : float
    lat2 : float
    long2 : float

