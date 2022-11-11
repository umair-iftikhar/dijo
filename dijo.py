import csv
import os
from datetime import datetime
from csv import DictWriter

now = datetime.now()
fields = ['log_type', 'log', 'project', 'date_time']

# Create the file path
filename = "logs/"+now.strftime("%m-%Y")+".csv"


def new_file():
    mydict =[{'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now}]
    
    if os.path.exists(filename):
        print("file already exist")
    else:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(mydict)


def new_entry(d):
    dict = d
    
    if os.path.exists(filename):
        with open(filename, 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=fields)
            dictwriter_object.writerow(dict)
            f_object.close()
    else:
        new_file()


new_entry({'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now})