import os
from typing import List
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Location(BaseModel):
    id: str
    lat: float
    lng: float

class CurrentLocations(BaseModel):
    timestamp: datetime
    currentLocations: List[Location]


csv_path = "locations.csv"


@app.on_event("startup")
async def startup_event():
    if not os.path.exists(csv_path):
        with open(csv_path, "w") as f:
            f.write("Vehicle,Timestamp,Lat,Lng\n")


@app.post("/")
async def save_locations(locations: CurrentLocations):
    locations_encoded = jsonable_encoder(locations)

    timestamp = locations_encoded["timestamp"]
    timestamp = correct_timestamp_format(timestamp)

    data_to_store_str = ""
    for loc in locations_encoded["currentLocations"]:
        single_location_data = []
        single_location_data.append(loc["id"])
        single_location_data.append(timestamp)
        single_location_data.append(str(loc["lat"])) 
        single_location_data.append(str(loc["lng"]) + "\n")

        data_to_store_str += ",".join(single_location_data)

    with open(csv_path, "a") as f:
        f.write(data_to_store_str)


def correct_timestamp_format(timestamp):
    dt_in_format = "%Y-%m-%dT%H:%M:%S"
    dt_out_format = "%Y-%m-%d %H:%M:%S"
    corrected_timestamp = datetime.strptime(timestamp, dt_in_format)
    
    return corrected_timestamp.strftime(dt_out_format)