import requests

API_KEY = "30f7efb56bd7dd08bbd1d59e61b7b8ea"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def main():
    print("Weather Forecast")
    print("=" * 16)
    print()

    city_name = input("Enter a city name to display weather: ")
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name

    weather_data = requests.get(complete_url).json()
    temperature = round((weather_data['main']['temp'] - 273.15), 1)
    feels_like = round((weather_data['main']['feels_like'] - 273.15), 1)
    wind_speed = round((weather_data['wind']['speed'] * 3.6), 1)
    description = weather_data['weather'][0]['description'].title()

    print(f"\nCurrent Weather for {weather_data['name']}")
    print(f"Temperature: {temperature} \u00B0C")
    print(f"Feels like: {feels_like} \u00B0C")
    print(f"Wind speed: {wind_speed} km/h")
    print(f"Description: {description}")


if __name__ == "__main__":
    main()
