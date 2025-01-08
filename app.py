'''
import streamlit as st
from Get_request import get_weather_data

st.title("Weather Information")

city_name = st.text_input("Enter city - ")

weather_data = get_weather_data(city_name=city_name)

if(weather_data):
    st.subheader("Weather Description")
    st.write(weather_data['weather'][0]['description'])
    st.write(weather_data['main']['temp'])
    # Display additional weather information
    st.subheader("Additional Information")
    st.write(f"Temperature: {weather_data['main']['temp']} °C")
    st.write(f"Humidity: {weather_data['main']['humidity']}%")
    st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
'''
import streamlit as st
from Get_request import get_weather_data

st.title("Weather Information")

# Input for city name
city_name = st.text_input("Enter city - ")

if city_name:
    weather_data = get_weather_data(city_name=city_name)
    
    if weather_data:
        st.subheader("Weather Description")
        st.write(weather_data['weather'][0]['description'])
            
        # Display additional weather information
        st.subheader("Additional Information")
        st.write(f"Temperature: {weather_data['main']['temp']} °C")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.error("Could not retrieve weather data. Please check the city name and try again.")

    