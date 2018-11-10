


class School(db.Model):
	__tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    dbn = db.Column(db.String, unique=True, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username 
    #have many ratings 
    #have many sub ratings through ratings 

    #has_many schoolattendances
    #has_many schoolSATs 

class Rating(db.Model):
	__tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    dbn = db.Column(db.String, unique=True, nullable=False)
    # some kind of dates
    #belongs to a school 
    #year
    # minimum is overall_rating (some are none, have to deal with that)
    # decide how granular.. I think we do it all and create ~6 rating_sub_categories

class InstructionalCore(db.Model):
	__tablename__ = 'instructional_cores'

    id = db.Column(db.Integer, primary_key=True)
    # dbn = db.Column(db.String, unique=True, nullable=False)
    # belongs_to a rating
    #we want these to be integers.. so preprocess as integers. 
    ic_1_1
    ic_1_2 
    ic_2_2

    
class SchoolCulture(db.Model):
	__tablename__ = 'school_culturess'

    id = db.Column(db.Integer, primary_key=True)
    # dbn = db.Column(db.String, unique=True, nullable=False)
    # belongs_to a rating
    sc_1_4
    sc_3_4


class SchoolImprovements(db.Model):
	__tablename__ = 'school_culturess'

    id = db.Column(db.Integer, primary_key=True)
    # belongs_to a rating

    si_1_3
    si_3_1
    si_4_1
    si_5_1

class SchoolAttendance(db.Model):
	__tablename__ = 'school_culturess'

	id = db.Column(db.Integer, primary_key=True)

	# belongs to a school 

	year #and yes, we need to process that in seed 
	school
	total_roster 
	percentage_absent 
	percentage_present 
	number_of absent 


class SchoolSAT(db.Model):
	__tablename__ = 'school_culturess'

	id = db.Column(db.Integer, primary_key=True)
	year = 
	#belongs to a school 
	school_id
	# school_dbn
	# school_name
	math_avg 
	reading_avg
	overall_avg 




# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False)
#     tweets = db.relationship('Tweet', backref='users', lazy=True)
#     def to_dict(self):
#         user = {'id': self.id, 'username': self.username, 'tweets': [tweet.to_dict() for tweet in self.tweets]}
#         return user

# class Tweet(db.Model):
#     __tablename__ = 'tweets'
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates="tweets")
#     def to_dict(self):
#         tweet = {'id': self.id, 'text': self.text, 'user_id': self.user.id, 'user': self.user.username}
#         return tweet