from sat_data import sat_data_list
from app import *
from ratings_data import ratings_list

import pdb
# creates the SATSchool and School models and tables in the database
db.create_all()

school_objects = []
sat_objects = []


for school in sat_data_list:
	if school['dbn']:
		new_school = School(dbn = school['dbn'], name = school['school_name'])
		school_objects.append(new_school)
		if school['test_takers'] != 's':
			new_satschool = SchoolSAT(dbn = school['dbn'], year = '2012', takers = int(school['test_takers']), reading_avg = int(school['reading_avg']), math_avg = int(school['math_avg']), writing_avg = int(school['writing_avg']))
			new_school.sats.append(new_satschool)
			sat_objects.append(new_satschool)



db.session.add_all(school_objects)
db.session.commit()
db.session.add_all(sat_objects)
db.session.commit()


# #download each of our tables and process...

# get ratings

# get dbn from sat data and add to school model



# get attendance


# get sat scores

# make a session, add to database
