# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func




#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Start with the homepage
@app.route("/")
def welcome():
    """List all available api routes."""
    # 1. List all the available routes
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

2. #####################################################################################
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using "date' as the key and "prcp" as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of only the last 12 months of data"""

    most_recent_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    first_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    rainfall = session.query(Measurements.date, Measurements.prcp).\
        filter(Measurements.date > first_date ).\
        order_by(Measurement.date.desc()).all()
    
    session.close()
     
     # # Create a list of dicts with `date` and `prcp` as the keys and values
    all_prcp = []
for date, prcp in rainfall:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)
     # # return JSON list of data

 return jsonify(all_prcp)
    
 ########################################################################################
@app.route("/api/v1.0/station")
def stations():
    
    """Return a list of stations"""
    st_list = session.query(station.name).all()

    session.close()

    # Convert list of tuples into normal list

  all_station = list(np.ravel(st_list))

return jsonify(all_stations)

###################################################################################################
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    last_year = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    first_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temperature = session.query(Measurements.date, Measurements.tobs).\
        filter(Measurements.date > first_date ).\
        order_by(Measurements.date).all()

    # Create a list of dicts with `date` and `tobs` as the keys and values
    temperature_totals = []
    for result in temperature:
        row = {}
        row["date"] = temperature[0]
        row["tobs"] = temperature[1]
        temperature_totals.append(row)

    return jsonify(temperature_totals)

 ######################################################################################
 # #  Go back one year from start date and go to end of data for Min/Avg/Max temp   

@app.route("/api/v1.0/<start>")
def start():  
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end =  dt.date(2017, 8, 23)
    results_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    trip1 = list(np.ravel(results_data))

    return jsonify(trip1)
  
 #######################################################################################
 # # Go back one year from start/end date and get Min/Avg/Max temp  
@app.route("/api/v1.0/<start>/<end>")
def (start,end):
start_date= dt.datetime.strptime(start, '%Y-%m-%d')
end_date= dt.datetime.strptime(end,'%Y-%m-%d')
last_year = dt.timedelta(days=365)
start = start_date-last_year
end = end_date-last_year
results_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
trip2 = list(np.ravel(results_data))


return jsonify(trip2)


if __name__ == '__main__':
      app.run(debug=True) 
