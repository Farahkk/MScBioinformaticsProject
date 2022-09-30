#!/usr/bin/python3

# Python program to convert text file to JSON
 
import json

filename = 'Downloads/Bioinformatics/MSc_Project/sample_files/12054.txt'
dic = {}

with open(filename, 'r') as f:
    #read lines from file and remove spaces to get valid data only
        for line in f:
            if ',' not in line:
                continue
            key, value = line.strip(';,\n').split(':', 1)
            dic[key] = value 
        print(json.dumps(dic, indent=2))