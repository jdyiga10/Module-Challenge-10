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
