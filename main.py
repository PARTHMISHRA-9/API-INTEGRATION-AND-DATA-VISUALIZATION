import requests
import matplotlib.pyplot as plt

# -------------------------------
# Configuration
# -------------------------------
API_KEY = "YOUR_API_KEY_HERE"
CITY = "Mumbai"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# -------------------------------
# Fetch Weather Data
# -------------------------------
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching data from API")
        return None

    return response.json()

# -------------------------------
# Process Data
# -------------------------------
def process_data(data):
    dates = []
    temperatures = []

    for entry in data["list"][:10]:  # first 10 records
        dates.append(entry["dt_txt"])
        temperatures.append(entry["main"]["temp"])

    return dates, temperatures

# -------------------------------
# Visualization
# -------------------------------
def plot_weather(dates, temps, city):
    plt.figure()
    plt.plot(dates, temps)
    plt.xticks(rotation=45)
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Forecast for {city}")
    plt.tight_layout()
    plt.show()

# -------------------------------
# Main Execution
# -------------------------------
def main():
    weather_data = fetch_weather_data(CITY)

    if weather_data:
        dates, temps = process_data(weather_data)
        plot_weather(dates, temps, CITY)

if __name__ == "__main__":
    main()
