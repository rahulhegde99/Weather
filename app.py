from flask import Flask, render_template, request
import requests
import json

# Initialize a new flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Get city and country from the UI form
        city = request.form['city']
        country = request.form['country']

        # API Key
        key = ""

        # Complete URL
        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={key}')
        
        # Convert the response to JSON
        weather_data = weather_url.json()

        # If the city(key) results in a 404 return 404.html
        if weather_data["cod"] == "404":
            return render_template('404.html', city=city, country=country)

        # Get temparature, humidity, windspeed, description and icon from Open Weather API
        temp = round(weather_data["main"]["temp"] - 273)
        humidity = round(weather_data["main"]["humidity"])
        wind_speed = round(weather_data["wind"]["speed"])
        desc = weather_data["weather"][0]["description"].upper()
        icon = weather_data["weather"][0]["icon"]

        # Render the result in result.html
        return render_template('result.html',temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, country=country, desc=desc, icon=icon)

    return render_template('index.html')

if __name__ == '__main__': 
    app.run()