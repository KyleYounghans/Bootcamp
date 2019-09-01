

from flask import Flask, render_template, redirect, jsonify

from flask_pymongo import PyMongo

import scrape_mars



# Use flask_pymongo to set up mongo connection

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
