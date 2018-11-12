
Next Steps:
-----------


To Do:
------
- deal with null values. some don't have the same rating
- convert strings ratings to a number rating system
- make stuff into years



school
- id
- DBN NUmber
- Name
- Neighborhood (find neighborhood?)




sample sheet
https://infohub.nyced.org/docs/default-source/default-document-library/quality-review-report-template_18-192875b773f6114eec90de65dbe1b1d8c0.pdf




ratings 2005 - 2017
https://data.cityofnewyork.us/Education/2005-2017-School-Quality-Review-Ratings/9n9z-hh9p
-raw number
-percentage
- features of the scores - look at those and see if any correclation


- school_dbn
-has DBN with school name directly built in
https://data.cityofnewyork.us/Education/2018-19-Quality-Review-School-List/2rr4-rfvc


sat_scores
https://data.cityofnewyork.us/Education/2012-SAT-Results/f9bf-2cp4




attendance 2012 - 2017
https://data.cityofnewyork.us/Education/2012-2017-Historical-Monthly-Grade-Level-Attendanc/wed3-5i35
- monthly
- yearly
- by school
- percentage of roster absence/preset
- and divided by grades (so we can do total, but have to aware of mixing middle and upper when talking about graduation rates)


graduation rate 2016-2017
https://data.cityofnewyork.us/Education/2016-2017-Graduation-Outcomes-School/nb39-jx2v


{'dbn': '01M292', 'school_name': 'HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES', 'test_takers': '29', 'reading_avg': '355', 'math_avg': '404', 'writing_avg': '363'}, {'dbn': '01M448', 'school_name': 'UNIVERSITY NEIGHBORHOOD HIGH SCHOOL', 'test_takers': '91', 'reading_avg': '383', 'math_avg': '423', 'writing_avg': '366'},
, overall_avg = int(school['math_avg']) + int(school['writing_avg']) + int(school['reading_avg'])