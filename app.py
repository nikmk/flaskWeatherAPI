from dotenv import load_dotenv
load_dotenv()

import os
import requests 
from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/<string:location>')
def index(location):
    
    url = os.environ['WEATHER_URL'] 
    link = url.format(location)
    r = requests.get(link).json()

    weather = {
        'city' : location,
        'description': r['weather'][0]['description'],
        'temperature': r['main']['temp'],
        'humidity': r['main']['humidity']
    }

    return jsonify(weather)



if __name__ == ('__main__' ):
    app.run()
