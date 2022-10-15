#!/usr/bin/python3

# Python program to convert text file to JSON
 
import json

filename = '12054.txt'
dic = {}
previousKey = ''

# This is our state machine to indicate if we are in one of the sequence
# blocks - to start we aren't

inSequence = False

#while(readFromFile(line))

with open(filename, 'r') as f:
        #read lines from file and remove spaces to get valid data only
        for line in f:
                line = line.strip(';,\n')
                #if ',' not in line:
                    #continue
                    #key, value = line.strip(';,\n').split(':', 1)
                #dic[key] = value 
                #print(json.dumps(dic, indent=2))
        
                if line == '//': #This indicates the end of a sequence block

                        inSequence = False

                # Regular expression /(Heavy|Light)?\s*Chain([.*])?:/
                elif line[0:5] == "Chain" or
                     line[0:11] == "Heavy Chain" or
                     line[0:11] == "Light Chain": # Start of a sequence block 

                        #remove-colon-from-end-of-line;
                        key = line.strip(':');
                        dic[key] = '';     # Initialize data storage 
        
                        inSequence = True;
        
                elif inSequence:    # We are within a sequence block
    
                        #cleanup(line):      # Strip whitespace and return character
                        dic[key] += line;  # Append sequence information to the data

                else:                # Normal line
                        if(len(line) > 1):
                                (key, value) = line.split(':', 1);
                                # Special case of note records where we add '-' and the previous line's key
                                if key[0:4] == 'Note':
                                        key += "-" + previousKey;
                                        dic[key] = value;
                                        continue
                                previousKey = key;     # Update the previous key to be the key from this line

                                dic[key] = value 
        print(json.dumps(dic, indent=2))
