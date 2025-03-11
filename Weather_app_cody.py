import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Weather in: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    else:
        print("Error fetching weather data")
def main():
    api_key = 'my_api_key_to_be_replaced'

    print("Welcome to the Avarn Weather App")
    city = input("Enter city name: ")

    get_weather(api_key, city)
if __name__ == '__main__':
    main()
