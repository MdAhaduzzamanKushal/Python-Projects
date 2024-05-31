import requests
from weatherbit.api import Api
from datetime import datetime

TOKEN = "---------------------"
chat_id = '------------'

# Initialize the Weatherbit API client with your API key
weather_api = Api("2de5477d74574c6bbbee678663d50437")

# Dhaka city's latitude and longitude coordinates
dhaka_lat = 23.8103
dhaka_lon = 90.4125

try:
    # Retrieve current weather data for Dhaka city
    weather_data = weather_api.get_current(lat=dhaka_lat, lon=dhaka_lon)

    # Extract weather details from the nested structure
    data = weather_data.json['data'][0]
    temperature = data['temp']
    weather_description = data['weather']['description']
    wind_speed = data['wind_spd']
    datetime_str = data['ob_time']  # Observation time

    # Convert observation time to a more readable format
    date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    formatted_datetime = date_time_obj.strftime('%Y-%m-%d %H:%M')

    # Compose message with real-time weather data
    message = (
        f"Real-time weather forecast for Dhaka City:\n"
        f"Current Location: Dhaka\n"
        f"Date and Time: {formatted_datetime}\n"
        f"Current Temperature: {temperature} °C\n"
        f"Weather Condition: {weather_description}\n"
        f"Wind Speed: {wind_speed} m/s"
    )

    # Send message
    send_message_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    send_message_response = requests.get(send_message_url).json()
    print(send_message_response)  # This sends the message

except Exception as e:
    print("An error occurred:", e)
