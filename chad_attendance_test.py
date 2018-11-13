from attendance_data import attendance_list 

# a_list = [{'School': '14K257', 'MonthCode': 4, 'CalMonth': 'Dec', 'SchoolYear': '2012 - 2013', 'GradeLevel': '0K', 'GradeSort': 0, 'RosterCount': 106, 'Present': 1456, 'Absent': 126, 'Released': 0}, {'School': '14K257', 'MonthCode': 4, 'CalMonth': 'Dec', 'SchoolYear': '2014 - 2015', 'GradeLevel': 'PK', 'GradeSort': -1, 'RosterCount': 66, 'Present': 974, 'Absent': 148, 'Released': 0}]

# established session connection: 
mega_list = []
for attendance in attendance_list: 
	new_dict = {}
	new_dict['School'] = attendance['School']
	new_dict['SchoolYear'] = attendance['SchoolYear'][-4:]
	new_dict['RosterCount'] = attendance['RosterCount']
	if not any(d['School'] == new_dict['School'] for d in mega_list):
		# print(i, "checks school:", new_dict, new_dict['School'])
		mega_list.append(new_dict)
	else:
		if not any(d['SchoolYear'] == new_dict['SchoolYear'] for d in mega_list):
			mega_list.append(new_dict)
			# print(i, "check year: ", new_dict, new_dict['SchoolYear'])
	# if new_dict['School']  and new_dict['SchoolYear']
print(mega_list)


# attendance only for 9th, 10th, 11th, 12th 
# group_by school, group_by year 
# by school 


# School 
# SchoolYear [-4:]
# RosterCount 


# school_years()
# 	get school years 

# school_grade()
# 	query with a school_grade

# list_of_school_bdns = []
# 'School_Year': '07/01/2006 12:00:00 AM', 'Start_Date': '11/01/2006 12:00:00"

# this year (for ratings) is the first date in 2016-2017 in other files will be 2016 in this file 






