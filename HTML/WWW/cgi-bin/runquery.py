#!/usr/bin/python3
import cgi
from pymongo import MongoClient
import sys
import re
import json
import cgitb
cgitb.enable()

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
def add_to_query(query_parts, key, value, yesno):
    query = ''
    if yesno == "yes":
        query = "{\"%s\" : {\"$regex\" : \".*%s.*\"}}" % (key, value)
    elif yesno == "no":
        query = "{\"%s\" : {\"$not\": {\"$regex\" : \".*%s.*\"}}}" % (key, value)

    if query != "":
        query_parts.append(query)
    return query_parts;

#-------------------------------------------------------------------------------
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
        
#-------------------------------------------------------------------------------
# Runs the query. Converts the JSON query into a dictionary and 
# runs it against the MongoDB database.
def run_query(collection, query):

    if query == '':
        # Return everything
        raw_results   = collection.find()
    else:
        # Convert JSON string to a dictionary and run query
        jsonquery = json.loads(query)
        raw_results   = collection.find(jsonquery)

    count = 0
    final_results = []
    for doc in raw_results:
        newdoc      = {}    
        count      += 1
        # Copy all the key/value pairs into the new document
        for key,value in doc.items():
            if key != '_id':
                newdoc[key] = value

        # Append this new document to the output
        final_results.append(newdoc)

    return(count, final_results)


    collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")

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




collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")

# Grab the form and the 'source' button value
# form  = cgi.FieldStorage()
# value = form.getvalue('source')

"""

Example of how you handle the yes/no/don't care buttons

Obviously, add_to_query(), combine_query_parts(), and run_query() are the routines
you have been using previously.

"""


# A list of the Yes/No/Don't care buttons' names in the HTML
yes_no_buttons = ['conj',
                  'bispecific',
                  'fusion']

# A list of the multi-value buttons (i.e. not just yes/no and the word MUST appear)
multi_value_buttons = ['Source_of_the_antibody']

# A list of buttons where we simply require the keyword to appear (or not appear)
# in the JSON, but don't care about the value (you don't have this at the moment in your HTML)
no_value_buttons = ['has_mutation']

# A dictionary mapping the button name to the field we need to search
fields = {'conj':'Format',
          'bispecific':'Format',
          'fusion':'Format',
          'Source_of_the_antibody':'Format',
          'has_mutation':'MutationH'}

# A dictionary mapping the button name to the keyword we will search for
keywords = {'conj':'conjugated',
            'bispecific':'bispecific',
            'fusion':'fusion'}

# Initialize the list of things we will query on
query_parts = []

# Obtain the information from the form
form = cgi.FieldStorage()

# Step through the yes/no buttons
for button in yes_no_buttons:
    value = form.getvalue(button)
    if(value is not None and value is not "don't care"):
        query_parts = add_to_query(query_parts, fields[button], keywords[button], value)
        #             The field name            ^^^ 
        #             The word we are looking for               ^^^
        #             We know it isn't "don't care", so it must be yes or no      ^^^

        
# Where we have other values which must be in the search we can work in the same way.
for button in multi_value_buttons:
    value = form.getvalue(button)
    if(value is not None and value is not "don't care"):
        query_parts = add_to_query(query_parts, fields[button], value, 'yes')
        #             The field name            ^^^ 
        #             The word we are looking for               ^^^
        #             Must always be yes                                ^^^
        
# Step through no-value buttons (i.e. those where we just need a field to be present
# or absent)
for button in no_value_buttons:
    value = form.getvalue(button)
    if(value is not None and value is not "don't care"):
        query_parts = add_to_query(query_parts, fields[button], '', value)
        #             The field name            ^^^ 
        #             The word we are looking for (blank)       ^^^
        #             It isn't "don't care", must be yes or no      ^^^

        
query   = combine_query_parts(query_parts)
(n_results, results) = run_query(collection, query)


# Construct some HTML
html = "<html>\n"
html += "  <head>\n"
html += "    <title>Result</title>\n"
html += "  </head>\n"
html += "  <body>\n"
html += "    <h1>Result</h1>\n"
html += "    <pre>\n"
# Iterate over the returned entries
for result in results:
    # In reality you need to do something here to start a row in your HTML table

    # Iterate over the key/value pairs
    for key,value in result.items():
        # Here you would test for the keys of interest that you want to use in the summary
        # table and print the html table data for those
        if (len(key)):
            html += key + ':' + value + "\n"
html += "    </pre>\n"
html += "    <p>\n";
html += "      Number of hits: " + str(n_results) + "\n";
html += "    </p>\n";
html += "  </body>\n"
html += "</html>\n"

# Print the output page
print ("Content-Type: text/html\n")
html = html.encode('ascii', errors='ignore');
html = html.decode()
print (html)
