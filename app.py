# import Flask and jsonify from flask
from flask import Flask, render_template, jsonify
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# initialize new flask app
app = Flask(__name__)

# tell your flask app to run with debug mode on
app.config['DEBUG'] = True


# add configurations and database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# connect SQLAlchemy to the configured flask app
db = SQLAlchemy(app)



class School(db.Model):
	__tablename__ = 'schools'
	id = db.Column(db.Integer, primary_key=True)
	dbn = db.Column(db.String, unique=True, nullable=False)
	# bn= db.Column(db.String, unique=True, nullable=False)
	name= db.Column(db.String, nullable= False)
	#has_many schoolSATs
	sats = db.relationship('SchoolSAT', back_populates='school')
	ratings= db.relationship('Rating', back_populates='school')

	def bn(self):
		new_string= self.db[2:6]
		return new_string

class SchoolSAT(db.Model):
	__tablename__ = 'school_sats'

	id = db.Column(db.Integer, primary_key=True)
	year = db.Column(db.String, nullable=False)
	dbn = db.Column(db.String, nullable=False )
	math_avg = db.Column(db.Integer, nullable=False)
	reading_avg = db.Column(db.Integer, nullable=False)
	# overall_avg = db.Column(db.Integer, nullable=False)
	writing_avg = db.Column(db.Integer, nullable=False)
	takers = db.Column(db.Integer, nullable=False)

	#belongs to a school
	school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
	school = db.relationship('School', back_populates="sats")


	# def __repr__(self):
	#     return '<User %r>' % self.username
	#have many ratings
	#have many sub ratings through ratings

	#has_many schoolattendances
	#has_many schoolSATs

# class Rating(db.Model):
# 	__tablename__ = 'sc6hools'
class Rating(db.model):
	__tablename__= 'ratings'
	id= db.Column(db.Integer, primary_key= True)
	bn= db.Column(db.String, unique= True, nullable= False)
	year= db.Column(db.Integer, nullable=False)
	school= relationship('School', back_populates='ratings')
	school_id= db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
	core= db.relationship('Core', uselist=False, back_populates= 'ratings')
	culture= db.relationship('Culture', uselist=False, back_populates= 'ratings')
	improvement= db.relationship('improvement', uselist=False, back_populates= 'ratings')



#     id = db.Column(db.Integer, primary_key=True)
#     dbn = db.Column(db.String, unique=True, nullable=False)
	# some kind of dates
	#belongs to a school
	#year
	# minimum is overall_rating (some are none, have to deal with that)
	# decide how granular.. I think we do it all and create ~6 rating_sub_categories

class Core(db.Model):
	__tablename__ = 'cores'
	id = db.Column(db.Integer, primary_key=True)
	ic_1_1= db.Column(db.Integer, nullable=False)
	ic_1_2= db.Column(db.Integer, nullable=False)
	ic_2_2= db.Column(db.Integer, nullable=False)
	rating= db.relationship('Rating', back_populates='core')
	rating_id= db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
	#     # dbn = db.Column(db.String, unique=True, nullable=False)
	#     # belongs_to a rating
	#     #we want these to be integers.. so preprocess as integers.


class Culture(db.Model):
	__tablename__ = 'cultures'
	id = db.Column(db.Integer, primary_key=True)
	sc_1_4= db.Column(db.Integer, nullable=False)
	sc_3_4= db.Column(db.Integer, nullable=False)
	rating= db.relationship('Rating', back_populates='culture')
	rating_id= db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
#     # dbn = db.Column(db.String, unique=True, nullable=False)
#     # belongs_to a rating


class Improvements(db.Model):
	__tablename__ = 'Improvements'
	id = db.Column(db.Integer, primary_key=True)
	si_1_3= db.Column(db.Integer, nullable=False)
	si_3_1= db.Column(db.Integer, nullable=False)
	si_4_1= db.Column(db.Integer, nullable=False)
	si_5_1= db.Column(db.Integer, nullable=False)
	rating= db.relationship('Rating', back_populates='improvement')
	rating_id= db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
	#     # belongs_to a rating

# class Attendance(db.Model):
# 	__tablename__ = 'attendances'
# 	id = db.Column(db.Integer, primary_key=True)
# 	month= db.Column(db.Integer, nullable= False)
# 	year= db.Column(db.Integer, nullable= False)
# 	total_rosters=

# 	# belongs to a school
# 	year #and yes, we need to process that in seed
# 	school
# 	total_roster
# 	percentage_absent
# 	percentage_present
# 	number_of absent


# run the server
if __name__ == "__main__":
	app.run()
