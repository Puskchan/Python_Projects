import requests
import os
from twilio.rest import Client

number = '+14153002875'

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_key")
account_sid = "ACe784d28194d2e3fefda3c914680f4614"
auth_token = os.environ.get("twillo_auth_token")

weather_params = {
    "lat": 31.1048,
    "exclude": "current,minutely,daily",
    "lon": 77.1734,
    "appid": api_key
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
for hourly_data in weather_slice:
    condition_code = hourly_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Take your umbrella ",
        from_=number,
        to='+919834279856'
    )
    print(message.status)
