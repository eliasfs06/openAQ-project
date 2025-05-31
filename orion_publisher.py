import requests
import os
from dotenv import load_dotenv

load_dotenv()

ORION_URL = os.getenv('ORION_URL')
FIWARE_SERVICE = os.getenv('FIWARE_SERVICE')
FIWARE_SERVICEPATH = os.getenv('FIWARE_SERVICEPATH')

headers = {
    'Content-Type': 'application/json',
    'Fiware-Service': FIWARE_SERVICE,
    'Fiware-ServicePath': FIWARE_SERVICEPATH
}

def publish_to_orion(data):
    response = requests.post(
        f"{ORION_URL}/v2/entities?options=upsert",
        json=data,
        headers=headers
    )

    print(f"Status Code: {response.status_code}, Response: {response.text}")
