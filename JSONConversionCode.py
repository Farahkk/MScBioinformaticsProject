#!/usr/bin/python3

# Python program to convert text file to JSON
 
import json

filename = '../data/12054.txt'
dic = {}

# This is our state machine to indicate if we are in one of the sequence
# blocks - to start we aren't

inSequence = False

#while(readFromFile(line))

with open(filename, 'r') as f:
    #read lines from file and remove spaces to get valid data only
        for line in f:
            #if ',' not in line:
                #continue
            #key, value = line.strip(';,\n').split(':', 1)
            #dic[key] = value 
        #print(json.dumps(dic, indent=2))
        
#while(readFromFile(line))          
            if line == '//': #This indicates the end of a sequence block

                inSequence = False

            elif line == "Chain" or line == "Heavy Chain" or line == "Light Chain": # Start of a sequence block 

            #remove-colon-from-end-of-line;
                 key = line;
                 data[key] = '';     # Initialize data storage 
        
                 inSequence = True;
        
            elif inSequence:    # We are within a sequence block
    
           #cleanup(line):      # Strip whitespace and return character
                data[key] += line;  # Append sequence information to the data

            else:                # Normal line
   
                (key, value) = line.strip(';,\n').split(':', 1);

           # Special case of note records where we add '-' and the previous line's key
            if key == 'Note[:]':
    
                key += "-" + previousKey;
      
                data[key] = value;
   
                previousKey = key;     # Update the previous key to be the key from this line
            
            #continue
        key, value = line.strip('; ,\n').split(':', 1)
        dic[key] = value 
        print(json.dumps(dic, indent=2))