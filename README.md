# Weather
Weather app built with Flask and [Open Weather API](http://openweathermap.org/)

Visit this link to view the app https://ubs-weather-app.herokuapp.com/

## How to Run App
- Register for an API key in [Open Weather API](http://openweathermap.org/) and replace the following in app.py
<pre>key="YOUR_API_KEY"</pre>

- Install all requirements
<pre>pip install -r requirements.txt</pre>

- Open command prompt and run app.py
<pre>python app.py</pre>

- Open the following in browser to view
<pre>http://127.0.0.1:5000/</pre>

## How to Run Unit Tests
- Open command prompt and run test.py
<pre>python test.py</pre>

## Some test cases
<pre>
Enter Valid City: Bengaluru
Enter Invalid City: Notarealcity
</pre>

<pre>
Enter Valid City: Mumbai
Enter Invalid City: Something
</pre>
