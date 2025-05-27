import os
from dotenv import load_dotenv
from openaq_client import OpenAQClient

def main():
    load_dotenv()
    api_key = os.getenv("OPENAQ_API_KEY")
    if not api_key:
        print("Erro: API Key da OpenAQ não encontrada no .env.")
        return

    client = OpenAQClient(api_key)

    print("Buscando localizações no Brasil...")
    locations = client.get_brazil_locations(limit=10)
    if not locations:
        print("Nenhuma localização encontrada.")
        return

    for loc in locations:
        print(f"\n Localização: {loc['id']} - {loc['name']}")
        try:
            sensors = client.get_sensor_location(loc['id'])
        except Exception as e:
            print(f"  Erro ao buscar sensores: {e}")
            continue

        if not sensors:
            print("  Nenhum sensor encontrado.")
            continue

        for sensor in sensors:
            sensor_id = sensor['id']
            param = sensor['parameter']['name']
            units = sensor['parameter']['units']
            print(f"  Sensor: {sensor_id} - {param} ({units})")
            try:
                measurements = client.get_measurements_by_sensor_id(sensor_id)
                if not measurements:
                    print("Nenhuma medição disponível.")
                    continue

                print("    Medições:")
                for m in measurements[:10]:  # limitar a 10 por sensor
                    value = m['value']
                    unit = m['parameter']['units']
                    datetime_from = m['period']['datetimeFrom']['local']
                    datetime_to = m['period']['datetimeTo']['local']
                    print(f"      • {datetime_from} → {datetime_to}: {value} {unit}")
            except Exception as e:
                print(f"    Erro ao buscar medições do sensor {sensor_id}: {e}")

if __name__ == "__main__":
    main()
