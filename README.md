# Weather Compare

A Python program that compares the current temperature of two cities using live data from the Open-Meteo API. It tells you which city is hotter and saves the results to a JSON file.

## Features
- Finds a city's location by name
- Fetches the live temperature
- Compares two cities
- Saves results to `results.json`

## API used
[Open-Meteo](https://open-meteo.com) (free, no API key needed)

## Install
1. Clone the repository:
   ```
   git clone https://github.com/hina-shykh/weather-compare.git
   cd weather-compare
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install the requirements:
   ```
   pip install requests
   ```

## Run
```
python main.py
```
Enter two city names when asked.

## Sample output
```
Enter first city: karachi
Enter second city: lahore
karachi: 25.9 °C
lahore: 20.8 °C
karachi is hotter by 5.1 °C
Saved to results.json
```

## Project files
- `main.py`: the program
- `results.json`: saved results
- `.gitignore`: files Git should ignore