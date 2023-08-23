#!/usr/bin/env python3
" " " Python program to populate json file " " "


import sys
import json
import pymongo
from pymongo import MongoClient

file = sys.argv[1]

def mongo_connect(user, password, host, path, clusterName, collectionName):
    """
    Call this with:
    collection = mongo_connect()
    """
   
    # Parameters for connecting to the database (which you can obtain from your Atlas account
    # See documentation at https://www.mongodb.com/docs/manual/reference/connection-string/
    options        = "?retryWrites=true&w=majority"

    #Connecting to the MongoDB database/collection
    url            = "mongodb+srv://" + user + ":" + password + "@" + host + path + options
    cluster        = MongoClient(url)
    db             = cluster[clusterName]
    collection     = db[collectionName]
    return collection


#file = sys.argv[0]

# Open JSON file, load the data as a dictionary and close the file
f = open(file)
record = json.load(f)
f.close()

collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")


# Insert the data
collection.insert_one(record)

#Read and print the data
#for record in collection.find():
#print(record)

# to run the file in the terminal

#for file in *.json
#do
#./populate.py $file
#done
