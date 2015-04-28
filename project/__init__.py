import os

from flask import Flask, jsonify
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

import urllib2

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import geocode
from project.models import Location

@app.route('/')
def home():
    return

@app.route('/<address_string>')
def return_geocoding(address_string):
    address_string = urllib2.unquote(address_string)
    gc = geocode.GeocodeCache(db)
    result = gc.geocode(address_string)
    return jsonify(result)