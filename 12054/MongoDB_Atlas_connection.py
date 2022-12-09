#!/usr/bin/env python3
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
    cluster        = MongoClient(url)
    db             = cluster[clusterName]
    collection     = db[collectionName]
    return collection