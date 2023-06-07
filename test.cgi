#!/usr/bin/python3
import cgi
from pymongo import MongoClient


# Grab the form and the 'source' button value
form  = cgi.FieldStorage()
value = form.getvalue('source')


# Construct some HTML
html = "<html>\n"
html += "  <head>\n"
html += "    <title>Result</title>\n"
html += "  </head>\n"
html += "  <body>\n"
html += "    <h1>Result</h1>\n"
html += "    <p>You clicked the <b>" + value + "</b> button.</p>\n"
html += "  </body>\n"
html += "</html>\n"

# Print the output page
print ("Content-Type: text/html\n")
print (html)
