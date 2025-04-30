import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        output = (
            f"Weather in {data['name']} ({data['sys']['country']}):\n"
            f"Temperature: {data['main']['temp']}°C\n"
            f"Weather: {data['weather'][0]['description'].capitalize()}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind Speed: {data['wind']['speed']} m/s\n"
        )

        print(output)

        # Save latest output
        with open("latest_output.txt", "w") as f:
            f.write(output)

        # Append to history
        with open("history_output.txt", "a") as f:
            f.write(output + "\n" + "-"*40 + "\n")

    else:
        print(f"\nError: {data.get('message', 'Unknown error')}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
