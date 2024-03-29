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
    #query_parts = add_to_query(query_parts, "Format", "bispecific", "yes")
    # Ensure that a MutationH record is present

    #query_parts = add_to_query(query_parts, "MutationH[1]", "", "yes")

 
    # Ensure that it's not a fusion protein
    #query_parts = add_to_query(query_parts, "Format", "fusion", "no")

    #query = combine_query_parts(query_parts)

    #print(query)


    # Source of the antibody:
    
    if query_parts == add_to_query(query_parts, "Format", "canine", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "caninized", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "chimeric", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "felinized", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "human", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "humanized", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "llama", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "mouse", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "murine", "yes"):
        query = combine_query_parts(query_parts)
        print(query)

    elif query_parts == add_to_query(query_parts, "Format", "rat", "yes"):
        query = combine_query_parts(query_parts)
        print(query)
    

    else:
        query_parts == add_to_query(query_parts, "Format", "resurfaced", "yes")
        query = combine_query_parts(query_parts)
        print(query)












    # Once you have a 'collection' variable (for your connection with the
    # MongoDB database) you can call run_query() against the database

    (n_results, results) = run_query(collection, query)

    # Iterate over the returned entries
    for result in results:
        # In reality you need to do something here to start a row in your HTML table

        # Iterate over the key/value pairs
        for key,value in result.items():
            # Here you would test for the keys of interest that you want to use in the summary
            # table and print the html table data for those
            if (len(key)):
                print(key + ':' + value)





    

"""
    # Query for the:

    #Identifier (INN "Request Number"):


#------------------------------------------------------------------------------------
    # Source of the antibody:
    
    
    # for canine:
    # Require the Format record contains 'canine'
    query_parts = add_to_query(query_parts, "Format", "canine", "yes")


    # for caninized:
    # Require the Format record contains 'caninized'
    query_parts = add_to_query(query_parts, "Format", "caninized", "yes")


    # for chimeric:
    # Require the Format record contains 'chimeric'
    query_parts = add_to_query(query_parts, "Format", "chimeric", "yes")


    # for felinized:
    # Require the Format record contains 'felinized'
    query_parts = add_to_query(query_parts, "Format", "felinized", "yes")


    # for human:
    # Require the Format record contains 'human'
    query_parts = add_to_query(query_parts, "Format", "human", "yes")


    # for humanized:
    # Require the Format record contains 'humanized'
    query_parts = add_to_query(query_parts, "Format", "humanized", "yes")


    # for llama:
    # Require the Format record contains 'llama'
    query_parts = add_to_query(query_parts, "Format", "llama", "yes")


    # for mouse:
    # Require the Format record contains 'mouse'
    query_parts = add_to_query(query_parts, "Format", "mouse", "yes")


    # for murine:
    # Require the Format record contains 'murine'
    query_parts = add_to_query(query_parts, "Format", "murine", "yes")


    # for rat:
    # Require the Format record contains 'rat'
    query_parts = add_to_query(query_parts, "Format", "rat", "yes")

    #also giving out bispecific (biparatopic) in the result???


    # for resurfaced:
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

    # results = run_query(collection, query)

