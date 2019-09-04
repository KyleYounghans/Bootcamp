# Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Route
@app.route("/")
def home(): 

    mars_data = mongo.db.mars_data.find_one()

    return render_template("index.html", mars_data=mars_data)

# Route Scrape
@app.route("/scrape")
def scrape(): 

    
    mars_data = mongo.db.mars_data
    mars_report = scrape_mars.news_scrape()
    mars_report = scrape_mars.image_scrape()
    mars_report = scrape_mars.facts_scrape()
    mars_report = scrape_mars.weather_scrape()
    mars_report = scrape_mars.hemispheres_scrape()
    mars_data.update({}, mars_report, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)