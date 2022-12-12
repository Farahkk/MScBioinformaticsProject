#!/usr/bin/env python3
# Python program to read
# json file

import json
import pymongo
from pymongo import MongoClient

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


# Open JSON file, load the data as a dictionary and close the file
f = open('12054.json')
record = json.load(f)
f.close()

collection = mongo_connect("FarahKhan", "Birkbeck1", "cluster0.xneqo1q.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")

# Insert the data
collection.insert_one(record)

# Read and print the data
for record in collection.find():
   print(record)


  
