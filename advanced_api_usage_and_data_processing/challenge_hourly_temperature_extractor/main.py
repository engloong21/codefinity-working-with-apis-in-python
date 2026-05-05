import requests

def print_first_five_paris_temperatures():
    # Your implementation goes here
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "hourly": "temperature_2m"
}
    response = requests.get (url, params=params)
    data = response.json()
    temps = data["hourly"]["temperature_2m"]
    first_five = temps[:5]

    pass
    
    # Iterate over the first five hourly temperature values and print each one
    for t in first_five:
        print(t)

print_first_five_paris_temperatures()




