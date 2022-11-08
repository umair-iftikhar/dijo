import csv
from datetime import datetime
from csv import DictWriter

now = datetime.now()
fields = ['log_type', 'log', 'project', 'date_time']

# Create the file path
filename = "logs/"+now.strftime("%m-%Y")+".csv"


def new_file():
    mydict =[{'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now}]
    # filename = now.strftime("%m-%Y")+".csv"
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
            
        # writing headers (field names)
        writer.writeheader()
            
        # writing data rows
        writer.writerows(mydict)

def new_entry():
    dict = {'log_type': 'S', 'log': 'New file created for month', 'project': 'diju', 'date_time': now}

    with open(filename, 'a') as f_object:

        dictwriter_object = DictWriter(f_object, fieldnames=fields)

        dictwriter_object.writerow(dict)

        f_object.close()


# new_file()
# new_entry()