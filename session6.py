# -*- coding: utf-8 -*-

#%%

with open("hello.txt", "w") as file:
    file.write("Hello MCSBT & MDBI")
    
#%%
    
import csv

def get_emails():
    
    list_of_emails = []
    
    with open("data/data.csv") as f:
        
        reader = csv.reader(f)
        
        for lines in reader:
            
            list_of_emails.append(lines[3])
            
    return list_of_emails

print(get_emails())

#%%

import json


with open("data/data.json") as file:
    
    json_data = json.load(file)

    for element in json_data:
        print(element["name"])

#%%
        
# Let’s get personal data from the person represented in luke.json. Print the name, height, eye_color, and mass.
        
import json

with open("data/luke.json") as file:
    
    json_data = json.load(file)
    
    print(json_data["name"])
    print(json_data["height"])

        
#%%
        
# Let’s create a format conversor. Our function convert_format will read all the data from data/data.csv and write it to a new JSON file named converted.json

import csv
import json

def converter():
    
    with open("data/data.csv") as csv_file:
        
        reader = csv.reader(csv_file)
        
        with open("converted.json", "w") as json_file:
            
            json_data = []
            
            for element in reader:
                
                json_dict = {
                  "id": element[0],
                  "name": element[1],
                  "last_name": element[2]
                }
                
                json_data.append(json_dict)
            
            json.dump(json_data, json_file)

converter()






















