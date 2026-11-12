import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    try:
        resp = requests.get(url, params={"name": city, "count": 1}, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("results")
        if not results:
            return None
        return results[0]["latitude"], results[0]["longitude"]
    except requests.RequestException:
        return None


def get_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()["current"]["temperature_2m"]
    except requests.RequestException:
        return None


if __name__ == "__main__":
    coords = get_coordinates("Karachi")
    if coords:
        print(get_temperature(coords[0], coords[1]))