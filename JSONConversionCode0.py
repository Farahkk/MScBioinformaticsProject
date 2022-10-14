#!/usr/bin/python3

# Python program to convert text file to JSON
 
import json

filename = '../data/12054.txt'
dic = {}

with open(filename, 'r') as f:
    #read lines from file and remove spaces to get valid data only
        for line in f:
            if ',' not in line:
                continue
            #key, value = line.strip(';,\n').split(':', 1)
            #dic[key] = value 
        #print(json.dumps(dic, indent=2))
        
        # This is our state machine to indicate if we are in one of the sequence
# blocks - to start we aren't
        inSequence = false;

        while(readFromFile(line))
        
       if(line == "//")  # This indicates the end of a sequence block

      inSequence = false;

       else if((line starts with "Chain")   ||  # Start of a sequence block
           (line starts with "Heavy Chain") ||
           (line starts with "Light Chain"))
       
       remove-colon-from-end-of-line;
       key = line;
       data[key] = '';     # Initialize data storage 
       inSequence = true;
        
       else if(inSequence)    # We are within a sequence block
    
       cleanup(line);      # Strip whitespace and return character
       data[key] += line;  # Append sequence information to the data

       else                   # Normal line
   
      (key, value) = split-on-colon(line);

      # Special case of note records where we add '-' and the previous line's key
       if(key starts with Note)
    
       key += "-" + previousKey;
      
       data[key] = value;
   
       previousKey = key;     # Update the previous key to be the key from this line


       key, value = line.strip(';,\n').split(':', 1)
            dic[key] = value 
       print(json.dumps(dic, indent=2))