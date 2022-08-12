import time
import requests


def find_the_weather(city_name):
    try:
        params = {  # asking weather in celcium
            'units': 'metric',
        }
        request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_name +
                               '&appid=af09bf8b6ec6d99b1e52b7812cff6124', params=params)
        json_data = request.json()
        condition = json_data['weather'][0]['main']
        temp = float(json_data['main']['temp'])
        min_temp = float(json_data['main']['temp_min'])
        max_temp = float(json_data['main']['temp_max'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%H:%M:%S", time.gmtime(
            json_data['sys']['sunrise']))
        sunset = time.strftime("%H:%M:%S",
                               time.gmtime(
                                   json_data['sys']['sunset']))

        result = {
            'City:': city_name,
            'General Condition:': condition,
            'Temperature:': str(temp) + ' ' + "°C",
            'Max temp.:': str(max_temp) + ' ' + "°C",
            'Min temp.:': str(min_temp) + ' ' + "°C",
            'Pressure:': str(pressure) + ' ' + 'mB',
            'Humidity:': str(humidity) + ' ' +'%',
            'Wind Speed:': str(wind) + ' ' + 'm/s',
            'Sunrise:': str(sunrise) + ' ' + 'GMT',
            'Sunset:': str(sunset) + ' ' + 'GMT'
        }

    except KeyError:
        return False

    return result




















