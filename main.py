import json
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


def get_city_temperature(city):
    coords = get_coordinates(city)
    if coords is None:
        return None
    return get_temperature(coords[0], coords[1])


def compare_cities(city1, city2):
    temp1 = get_city_temperature(city1)
    temp2 = get_city_temperature(city2)

    if temp1 is None or temp2 is None:
        print("Could not get data. Check the city names or your internet.")
        return None

    print(f"{city1}: {temp1} °C")
    print(f"{city2}: {temp2} °C")

    if temp1 > temp2:
        print(f"{city1} is hotter by {temp1 - temp2:.1f} °C")
    elif temp2 > temp1:
        print(f"{city2} is hotter by {temp2 - temp1:.1f} °C")
    else:
        print("Both cities have the same temperature")

    return {city1: temp1, city2: temp2}

def save_results(results, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    first = input("Enter first city: ")
    second = input("Enter second city: ")
    results = compare_cities(first, second)
    if results:
        save_results(results)