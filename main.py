import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_temperature_by_date(date):
    data = get_weather_data()
    if data:
        for item in data['list']:
            if date in item['dt_txt']:
                return item['main']['temp']
        print("No temperature data available for the given date.")
    return None

def get_wind_speed_by_date(date):
    data = get_weather_data()
    if data:
        for item in data['list']:
            if date in item['dt_txt']:
                return item['wind']['speed']
        print("No wind speed data available for the given date.")
    return None

def get_pressure_by_date(date):
    data = get_weather_data()
    if data:
        for item in data['list']:
            if date in item['dt_txt']:
                return item['main']['pressure']
        print("No pressure data available for the given date.")
    return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            date = input("Enter the date (yyyy-mm-dd): ")
            temperature = get_temperature_by_date(date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")
        
        elif option == '2':
            date = input("Enter the date (yyyy-mm-dd): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif option == '3':
            date = input("Enter the date (yyyy-mm-dd): ")
            pressure = get_pressure_by_date(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")

        elif option == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
