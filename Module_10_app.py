# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
from dateutil.relativedelta import relativedelta



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///hawaii.sqlite")
metadata = MetaData()
metadata.reflect(bind=engine)

Base = automap_base(metadata=metadata)
Base.prepare()



# reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Save references to each table


# Create our session (link) from Python to the DB
session = Session(engine)
measurements = session.query(Measurement).all()
session.close()


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/measurements<br/>"
        f"/api/v1.0/stations"
    )

@app.route("/api/v1.0/measurements")
def get_measurements():
    """Return a list of measurements including date and prcp"""
    # Query all measurements
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert the query results to a dictionary
    measurements_data = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        measurements_data.append(measurement_dict)

    return jsonify(measurements_data)

@app.route("/api/v1.0/stations")
def get_stations():
    """Return a list of stations."""
    # Query all stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    stations_data = [station[0] for station in results]

    return jsonify(stations_data)

if __name__ == '__main__':
    app.run(debug=True)