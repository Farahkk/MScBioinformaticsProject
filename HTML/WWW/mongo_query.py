#!/usr/bin/env python3
import pymongo
from pymongo import MongoClient
import sys
import re
import json



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

    # Require the Format record contains 'bispecific'
    query_parts = add_to_query(query_parts, "Format", "bispecific", "yes")
    # Ensure that a MutationH record is present
    query_parts = add_to_query(query_parts, "MutationH", "", "yes")
    # Ensure that it's not a fusion protein
    query_parts = add_to_query(query_parts, "Format", "fusion", "no")

    query = combine_query_parts(query_parts)

    print(query)

    # Once you have a 'collection' variable (for your connection with the
    # MongoDB database) you can call run_query() against the database
    # results = run_query(collection, query)
