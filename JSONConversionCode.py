#!/usr/bin/python3

# Python program to convert text file to JSON
 
import json

# the file to be converted to
# json format
file = 'Downloads/Bioinformatics/MSc_Project/sample_files/12054.txt'

 
# dictionary where the data from
# text file will be stored
dict = {}
 
# read from file 
with open(file) as f:
 
    for line in f:
        #read lines from file and remove spaces to get valid data only
        if ',' not in line:
            continue
        key, desc = line.strip().split(None,1)
        dict[key] = desc.strip()


print(json.dumps(dict, indent=2))