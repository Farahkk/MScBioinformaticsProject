#!/usr/bin/env python3
import pymongo
from pymongo import MongoClient
import sys
import re
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






def add_to_query(query_parts, key, value, yesno):
    query = ''
    if yesno == "yes":
        query = "{\"%s\" : {\"$regex\" : \".*%s.*\"}}" % (key, value)
    elif yesno == "no":
        query = "{\"%s\" : {\"$not\": {\"$regex\" : \".*%s.*\"}}}" % (key, value)

    if query != "":
        query_parts.append(query)
    return query_parts;

#-------------------------------------------------------------------------
# Combines the individual query parts into one query
def combine_query_parts(query_parts):
    query = ''

    if len(query_parts) == 0:
        # Everything is don't care so we will need the whole list back
        return('')
    elif len(query_parts) == 1:
        # Only one item so no ANDing
        return(query_parts[0])

    line_num = 0                           # Used to count through the lines
    query    = "{ \"$and\" : [\n"          # Initialize ANDing
    for line in query_parts:
        query    += "         " + line     # Add this line (spaces are just formatting for debugging!)
        line_num += 1
        if line_num < (len(query_parts)):
            # Anything other than the last line we add a comma
            query += ",\n"
        else:
            query += "\n"
    query += "]}"                          # Finish the ANDing
 
    return(query)


        
#-------------------------------------------------------------------------
# Runs the query. Converts the JSON query into a dictionary and 
# runs it against the MongoDB database.
def run_query(collection, query):

    if query == '':
        # Return everything
        results   = collection.find()
    else:
        # Convert JSON string to a dictionary and run query
        jsonquery = json.loads(query)
        results   = collection.find(jsonquery)
        
    return(results)

#-------------------------------------------------------------------------
if __name__ == "__main__":
    query_parts = []

    # Query for the:

    #Identifier (INN "Request Number"):
    """

    # Source of the antibody:
    # Require the Format record contains 'canine'
    query_parts = add_to_query(query_parts, "Format", "canine", "yes")

    # Require the Format record contains 'caninized'
    query_parts = add_to_query(query_parts, "Format", "caninized", "yes")

    # Require the Format record contains 'chimeric'
    query_parts = add_to_query(query_parts, "Format", "chimeric", "yes")

    # Require the Format record contains 'felinized'
    query_parts = add_to_query(query_parts, "Format", "felinized", "yes")

    # Require the Format record contains 'human'
    query_parts = add_to_query(query_parts, "Format", "human", "yes")

    # Require the Format record contains 'humanized'
    query_parts = add_to_query(query_parts, "Format", "humanized", "yes")

    # Require the Format record contains 'llama'
    query_parts = add_to_query(query_parts, "Format", "llama", "yes")

    # Require the Format record contains 'mouse'
    query_parts = add_to_query(query_parts, "Format", "mouse", "yes")

    # Require the Format record contains 'murine'
    query_parts = add_to_query(query_parts, "Format", "murine", "yes")

    # Require the Format record contains 'rat'
    query_parts = add_to_query(query_parts, "Format", "rat", "yes")

    # Require the Format record contains 'resurfaced'
    query_parts = add_to_query(query_parts, "Format", "resurfaced", "yes")





    # Nature of the antibody:
    # for conjugated
    # Require the Format record contains 'conjugated'
    query_parts = add_to_query(query_parts, "Format", "conjugated", "yes")

    # Ensure that it's not a conjugated protein
    query_parts = add_to_query(query_parts, "Format", "conjugated", "no")


    # for bispecific
    # Require the Format record contains 'bispecific'
    query_parts = add_to_query(query_parts, "Format", "bispecific", "yes")

    # Ensure that it's not a bispecific protein
    query_parts = add_to_query(query_parts, "Format", "bispecific", "no")


    # for fusion
    # Require the Format record contains 'fusion'
    query_parts = add_to_query(query_parts, "Format", "fusion", "yes")

    # Ensure that it's not a bispecific protein
    query_parts = add_to_query(query_parts, "Format", "fusion", "no")



    #Fusion with:


    #Enter ID (e.g. clone name, lab code, etc.):


    #Antibody type:
    #Heavy Chain:
    #IgG1
    # Require the Type record contains 'IgG1'
    query_parts = add_to_query(query_parts, "Format", "IgG1", "yes")

    #IgG2
    # Require the Type record contains 'IgG2'
    query_parts = add_to_query(query_parts, "Format", "IgG2", "yes")

    #IgG3
    # Require the Type record contains 'IgG3'
    query_parts = add_to_query(query_parts, "Format", "IgG3", "yes")

    #IgG4
    # Require the Type record contains 'IgG4'
    query_parts = add_to_query(query_parts, "Format", "IgG4", "yes")

    #Fv
    # Require the Type record contains 'Fv'
    query_parts = add_to_query(query_parts, "Format", "Fv", "yes")




    """




    # Require the Format record contains 'bispecific'
    query_parts = add_to_query(query_parts, "Format", "bispecific", "yes")
    # Ensure that a MutationH record is present
    query_parts = add_to_query(query_parts, "MutationH", "", "yes")
    # Ensure that it's not a fusion protein
    query_parts = add_to_query(query_parts, "Format", "fusion", "no")

    query = combine_query_parts(query_parts)

    #print(query)

    collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")

    # Once you have a 'collection' variable (for your connection with the
    # MongoDB database) you can call run_query() against the database
    #results = run_query(collection, query)
    results = run_query(collection, '')
    #print(results)
    for key,value in results.items():
        if (len(key)):
            print(key + ':' + value)