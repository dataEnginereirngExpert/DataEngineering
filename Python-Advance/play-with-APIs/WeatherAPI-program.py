import requests
import csv

# Step 1: API URL
url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current_weather=true"

# Step 2: Make API request
response = requests.get(url)

# Error handling
if response.status_code != 200:
    print("API Error:", response.status_code)
    exit()

data = response.json()

# Step 3: Extract data
current = data["current_weather"]

weather_info = {
    "temperature": current["temperature"],
    "windspeed": current["windspeed"],
    "winddirection": current["winddirection"],
    "weather_code": current["weathercode"],
    "time": current["time"]
}

# Step 4: Save to CSV
with open("weather_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=weather_info.keys())
    writer.writeheader()
    writer.writerow(weather_info)

print("Weather data saved to weather_data.csv")
