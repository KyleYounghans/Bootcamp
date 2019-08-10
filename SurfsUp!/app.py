import numpy as np

import sqlalchemy

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

import datetime as dt



# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False}, echo=True)

# Automap Database

Base = automap_base()

# Prepare Tables

Base.prepare(engine, reflect=True)


# Create Variables for Tables

Measurement = Base.classes.measurement

Station = Base.classes.station

# Link Python to the DB

session = Session(engine)


# Create an app, being sure to pass __name__

app = Flask(__name__)

# Define what to do when a user hits the index route

@app.route("/")

def welcome():

    """List all available api routes."""
    
    return"""
    <html>

    <h2>Available API routes for Honolulu, HI API</h2>
    <br>
    <br>
    <h4>Precipitation in the Last Year:&nbsp;<a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></h4>

    <h4>Available Stations:&nbsp;<a href="/api/v1.0/stations">/api/v1.0/stations</a></h4>
    
    <h4>Temperature Observations from the Previous Year:&nbsp;<a href="/api/v1.0/tobs">/api/v1.0/tobs</a></h4>
   
    <h4>List of TMIN, TAVG, TMAX Starting with the Date Provided:&nbsp;<a href="/api/v1.0/2017-08-22">/api/v1.0/2017-08-22</a></h4>
    &emsp;Note: You can replace the dates in the URL (Use the same format of Year-Month-Day).
    <br>
    <h4>List of TMIN, TAVG, TMAX for the Each Date Between the Start and End Dates:&nbsp;<a href="/api/v1.0/2010-01-01/2017-08-23">/api/v1.0/2010-01-01/2017-08-23</a></h4>
    &emsp;Note: You can replace the dates in the URL (Use the same format of Year-Month-Day).
 
    </html>
    
    """

    
# Define what to do when a user hits the /api/v1.0/precipitation route

@app.route("/api/v1.0/precipitation")

def precipitation():


    precip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    precip = precip[0]

    lastyear = dt.datetime.strptime(precip, "%Y-%m-%d") - dt.timedelta(days=366)

    precip_Q = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= lastyear).all()

    precip_D = dict(precip_Q)

    return jsonify(precip_D)


# Define what to do when a user hits the /api/v1.0/stations route

@app.route("/api/v1.0/stations")

def stations(): 

    stations_Q =  session.query(Measurement.station).group_by(Measurement.station).all()

    stations_L = list(np.ravel(stations_Q))

    return jsonify(stations_L)


# Define what to do when a user hits the /api/v1.0/tobs route

@app.route("/api/v1.0/tobs")

def tobs(): 

    tobs_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    tobs_date = tobs_date[0]

    lastyear_tobs = dt.datetime.strptime(tobs_date, "%Y-%m-%d") - dt.timedelta(days=366)

    tobs_Q = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= lastyear_tobs).all()

    tobs_L = list(tobs_Q)

    return jsonify(tobs_L)

# Define what to do when a user hits the /api/v1.0/<start> route
@app.route("/api/v1.0/<start>")

def start(start=None):

    start_Q = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).group_by(Measurement.date).all()

    start_L =list(start_Q)

    return jsonify(start_L)

# Define what to do when a user hits the /api/v1.0/<start>/<end> route
 
@app.route("/api/v1.0/<start>/<end>")

def start_end(start=None, end=None):


    start_end_Q = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()

    start_end_L=list(start_end_Q)

    return jsonify(start_end_L)



if __name__ == '__main__':

    app.run(debug=True)