from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        key = ""
        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={key}')
        weather_data = weather_url.json()
        if weather_data["cod"] == "404":
            return render_template('404.html', city=city, country=country)
        temp = round(weather_data["main"]["temp"] - 273)
        humidity = round(weather_data["main"]["humidity"])
        wind_speed = round(weather_data["wind"]["speed"])
        desc = weather_data["weather"][0]["description"].upper()
        icon = weather_data["weather"][0]["icon"]
        #icon_src = "http://openweathermap.org/img/wn/{icon}.png"
        return render_template('result.html',temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, country=country, desc=desc, icon=icon)

    return render_template('index.html')

if __name__ == '__main__': 
    app.run()
