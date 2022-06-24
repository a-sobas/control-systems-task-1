import requests
from datetime import datetime
import numpy as np
import time


while True:
    id_max = np.random.randint(1, 5)

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "currentLocations": [
            {
                "id": str(i),
                "lat": np.random.uniform(-90, 90),
                "lng": np.random.uniform(-180, 180)
            } for i in range(1, id_max + 1)
        ]
    }

    response = requests.post("http://127.0.0.1:8000/", json=data)

    print("Request response status code:", response.status_code)

    time.sleep(10)