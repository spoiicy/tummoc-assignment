from fastapi import FastAPI
import schema
import math

app = FastAPI()

@app.post("/distance")
def calculate_distance(coordinates : schema.coordinateRequest):
    x1 = coordinates.lat1
    y1 = coordinates.long1
    x2 = coordinates.lat2
    y2 = coordinates.long2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return {"distance": distance}