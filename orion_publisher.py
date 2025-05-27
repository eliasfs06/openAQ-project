import requests
import json

class OrionPublisher:
    def __init__(self, base_url="http://localhost:1026/v2/entities", service="smart", service_path="/"):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Fiware-Service": service,
            "Fiware-ServicePath": service_path
        }

    def upsert_entity(self, entity: dict):
        entity_id = entity["id"]
        get_url = f"{self.base_url}/{entity_id}"

        response = requests.get(get_url, headers=self.headers)
        if response.status_code == 200:
            patch_url = f"{get_url}/attrs"
            requests.patch(patch_url, headers=self.headers, data=json.dumps(entity))
        else:
            requests.post(self.base_url, headers=self.headers, data=json.dumps(entity))
