# importing the csv module
import csv

from datetime import datetime

now = datetime.now()

	
# my data rows as dictionary objects
mydict =[{'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now}]
	
# field names
fields = ['log_type', 'log', 'project', 'date_time']
	
# name of csv file
filename = now.strftime("%m-%Y")+".csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
	# writing headers (field names)
	writer.writeheader()
		
	# writing data rows
	writer.writerows(mydict)
