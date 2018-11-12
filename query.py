
from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from app import School, SchoolSAT 
# initialize new flask app
app = Flask(__name__)

# tell your flask app to run with debug mode on
app.config['DEBUG'] = True


# add configurations and database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# connect SQLAlchemy to the configured flask app
db = SQLAlchemy(app)
