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



























