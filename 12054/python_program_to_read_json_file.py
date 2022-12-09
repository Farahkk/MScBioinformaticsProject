#!/usr/bin/python3

import sys 
import json
import pymongo
from pymongo import MongoClient

def mongo_connect():
    """
    Call this with:
    collection = mongo_connect()
    """
    
    # Parameters for connecting to the database (which you can obtain from your Atlas account
    # See documentation at https://www.mongodb.com/docs/manual/reference/connection-string/
    #user           = "MyUserName"
    #password       = "MyPassword"
    #host           = "cluster0.example.mongodb.net"
    #path           = "/AntibodyBasedDrugs"
    #options        = "?retryWrites=true&w=majority"
    #clusterName    = "MyClusterName"
    #collectionName = "MyCollectionName"
    user           = "FarahKhan"
    password       = "Birkbeck1"
    host           = "cluster0.example.mongodb.net"
    path           = "/AntibodyBasedDrugs"
    options        = "?retryWrites=true&w=majority"
    clusterName    = "Cluster0"
    collectionName = "Database Deployments"

    #Connecting to the MongoDB database/collection
    url            = "mongodb+srv://" + user + ":" + password + "@" + host + path + options
    print (url)
    cluster        = MongoClient(url)
    db             = cluster[clusterName]
    collection     = db[collectionName]
    return collection

collection = mongo_connect()
exit()
# Python program to read
# json file
  
#import sys 
#import json

#filename = sys.argv[-1]

# Opening JSON file
f = open('12054.json')
  
# returns JSON object as 
# a dictionary
record = json.load(f)
print(record)

# Iterating through the json
# list
#for i in data['emp_details']:
    #print(i)
  
# Closing file
f.close()

rec_id1 = collection.insert_one(record)