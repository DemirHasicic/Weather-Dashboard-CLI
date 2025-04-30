# 🌦️ Weather Dashboard (CLI)

A simple Python project that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api). Built to demonstrate RESTful API usage, JSON parsing, and clean CLI interaction.

---

## 🚀 Features

- Get real-time weather data for any city 🌍
- Shows:
  - City and country
  - Temperature in °C
  - Weather description
  - Humidity %
  - Wind speed in m/s
- Saves:
  - `latest_output.txt` → most recent result (overwritten)
  - `history_output.txt` → all past results (appended)
- Uses `.env` to securely store API keys 🔐

---

## 🛠 Technologies Used

- Python 3
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- OpenWeatherMap RESTful API

---

## 🧪 Example Output
Weather in Sarajevo (BA):
Temperature: 22.95°C
Weather: Few clouds
Humidity: 38%
Wind Speed: 3.09 m/s

