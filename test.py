import requests

BASE = "http://127.0.0.1:8000/"

data = {
    "timestamp": "2022/06/10 08:00:00",
    "currentLocations": [
    {
        "id": "1",
        "lat": 52.1,
        "lng": 16.4
    },
    {
        "id": "2",
        "lat": 52.2,
        "lng": 17.8
    },
    {
        "id": "3",
        "lat": 52.2,
        "lng": 17.8
    }
    ]
}


r = response = requests.post(BASE, json=data)

print(r.status_code)