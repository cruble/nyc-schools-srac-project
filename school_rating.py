<<<<<<< HEAD
# import requests
# r= requests.get('https://data.cityofnewyork.us/resource/i3q5-gtjn').json()
# school_rating= r

import pandas as pd
school_rating= pd.read_csv('school_ratings.csv')
school_rating


#from csv tutorial, keep getting syntax error in reader
# import csv
# import sys
# # def school_rating():
# f= open('school_ratings.csv', 'rb')
# reader= csv.reader(f)
# for row in reader
# print row
=======
import requests
r= requests.get('https://data.cityofnewyork.us/resource/i3q5-gtjn').json()
school_rating= r
school_rating
>>>>>>> 1b5a49f13bf6f4149c4a0d61fa5e7bdf8667ec7e
