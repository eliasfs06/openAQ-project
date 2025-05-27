class NGSIFormatter:
    def format_measurement(self, measurement: dict, city: str, location: str):
        parameter_data = measurement.get("parameter", {})
        period = measurement.get("period", {})
        datetime_from = period.get("datetimeFrom", {}).get("local")
        datetime_to = period.get("datetimeTo", {}).get("local")

        parameter = parameter_data.get("name")
        unit = parameter_data.get("units")
        value = measurement.get("value")

        entity_id = f"AirQuality:{city}:{location}:{parameter}".replace(" ", "_")

        return {
            "id": entity_id,
            "type": "AirQualityObserved",
            "parameter": {
                "type": "Text",
                "value": parameter
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
            "location": {
                "type": "Text",
                "value": location
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
