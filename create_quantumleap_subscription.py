import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

ORION_URL = os.getenv('ORION_URL')
QUANTUMLEAP_URL = os.getenv('QUANTUMLEAP_URL')

# Orion e QuantumLeap endpoints reais
ORION_URL = f"{ORION_URL}/v2/subscriptions"
QUANTUMLEAP_URL = f"{QUANTUMLEAP_URL}/v2/notify"

# Headers FIWARE
headers = {
    "Content-Type": "application/json",
    "Fiware-Service": "openaq",
    "Fiware-ServicePath": "/"
}

# Corpo da subscription
subscription = {
    "description": "Store AirQuality data in QuantumLeap",
    "subject": {
        "entities": [
            {
                "idPattern": "AirQualityObserved:.*",
                "type": "AirQualityObserved"
            }
        ]
    },
    "notification": {
        "http": {
            "url": QUANTUMLEAP_URL
        },
        "attrs": ["dateObserved", "pm10", "pm25", "no2"]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}

# Enviando para o Orion
response = requests.post(ORION_URL, headers=headers, json=subscription)

# Resultado
if response.status_code in [200, 201, 204]:
    print("✅ Subscription criada com sucesso!")
else:
    print(f"❌ Erro ({response.status_code}): {response.text}")