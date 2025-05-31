import re
import unicodedata

class NGSIFormatter:
    def normalize_id(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
        return re.sub(r'\W+', '_', text)

    def format_measurement(self, measurement: dict, city: str):
        parameter_data = measurement.get("parameter", {})
        period = measurement.get("period", {})
        datetime_from = period.get("datetimeFrom", {}).get("local")
        datetime_to = period.get("datetimeTo", {}).get("local")

        parameter = parameter_data.get("name")
        unit = parameter_data.get("units")
        value = measurement.get("value")

        entity_id = f"AirQualityObserved:{self.normalize_id(city)}:{parameter}".replace(" ", "_")

        return {
            "id": entity_id,
            "type": "AirQualityObserved",
            "parameter": {
                "type": "Text",
                "value": parameter
            },
            "dateObserved": {
                "type": "DateTime",
                "value": measurement['period']['datetimeTo']['utc']  # Novo!
            },
            "value": {
                "type": "Number",
                "value": value
            },
            "unit": {
                "type": "Text",
                "value": unit
            },
            "city": {
                "type": "Text",
                "value": city
            },
            "dateObservedFrom": {
                "type": "DateTime",
                "value": datetime_from
            },
            "dateObservedTo": {
                "type": "DateTime",
                "value": datetime_to
            }
        }
