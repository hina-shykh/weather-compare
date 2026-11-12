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


if __name__ == "__main__":
    print(get_coordinates("Karachi"))