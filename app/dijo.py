import csv
import os
from datetime import datetime
from csv import DictWriter

now = datetime.now()
fields = ['log_type', 'log', 'project', 'date_time']

# Create the file path
filename = "logs/"+now.strftime("%m-%Y")+".csv"


###########################################
# Check file exist, else create new file. #
###########################################

def new_file():
    mydict =[{'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now}]
    
    if os.path.exists(filename):
        print("file already exist")
    else:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(mydict)



####################################################
# Validate an entry #
####################################################

def validate_entry(en):
    
    # define log type (log_type)
    if en[0].lower() == "n" or en[0].lower() == "t" or en[0].lower() == "e" or en[0].lower() == "d" or en[0]=="!": 
        return True
    else:
        return False







####################################################
# Convert string into CSV Columns and return Dict. #
####################################################

def create_entry(en):
    
    # define date (date_time)
    dict = {"date_time": now}
    
    # define log type (log_type)
    if validate_entry(en): 
        dict["log_type"] = en[0].upper()
    else:
        raise Exception("String is not following the guideline. Please refer Guide.")

    # define log (log)
    dict["log"] = en[1:].replace(" ", "", 1)

    # define project name (project)
    if "@" in en:
        dict["project"] = en.rsplit(" @")[1].split(" ")[0]

    return dict


############################
# Enter log into CSV File  #
############################

def new_entry(d):
    dict = d
    
    if os.path.exists(filename):
        with open(filename, 'a', encoding='utf-8', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=fields)
            dictwriter_object.writerow(dict)
            f_object.close()
    else:
        new_file()