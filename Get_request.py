import requests 
def get_weather_data(city_name : str):
    api_key = "5a790b6cd6ea3efba8aa85df310df8da"
    url = "https://api.openweathermap.org/data/2.5/weather"

    #set up the parameters for the API requests
    params = {
        'q' : city_name,
        'appid' : api_key,
        'units' : 'metric'
    }

    # Make the request to the OpenWeatherMap API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        # Handle errors (e.g., city not found)
        return {"error": response.json().get("message", "An error occurred")}

#Example  
city = "London"
weather = get_weather_data(city)
print(weather)