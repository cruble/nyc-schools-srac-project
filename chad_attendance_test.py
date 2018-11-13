from attendance_data import attendance_list 



# established session connection: 
grade_12 = []

for attendance in attendance_list: 
	if attendance['GradeLevel'] =='12':
		grade_12.append(attendance)

print(grade_12)

# attendance only for 9th, 10th, 11th, 12th 
# group_by school, group_by year 
# by school 



# school_years()
# 	get school years 

# school_grade()
# 	query with a school_grade

# list_of_school_bdns = []
# 'School_Year': '07/01/2006 12:00:00 AM', 'Start_Date': '11/01/2006 12:00:00"

# this year (for ratings) is the first date in 2016-2017 in other files will be 2016 in this file 






