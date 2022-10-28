#!/usr/bin/python3
# Python program to convert text file to JSON

# for file in *.txt
# do
#     ./JSONConversionCode.py $file > `basename $file .txt`.json
# done

import sys
import fileinput
import json
import re

#filename = input('Enter a file path: ')
#filename = sys.argv[-1]
#for arg in sys.argv[1:]:    # [0] is the program name.
    print(arg)

dic = {}
previousKey = ''

# This is our state machine to indicate if we are in one of the sequence
# blocks - to start we aren't

inSequence = False

# using fileinput() to call filename in the terminal
for line in fileinput.input(encoding="utf-8"):
    process(line)

for arg in sys.argv[1:]:    # [0] is the program name.
    print(arg)    

#while(readFromFile(line))

with open(filename, 'r') as f:
        #read lines from file and remove spaces to get valid data only
        for line in f:
                line = line.strip(';,\n')
        
                if line == '//': #This indicates the end of a sequence block

                        inSequence = False

                # Regular expression /(Heavy|Light)?\s*Chain([.*])?:/
                
                # Heavy Chain[1] or Light Chain[1] or Chain[2-3-4-5]
                
                # re.findall(r((Heavy|Light)?\s*Chain(/[.*/])?)):
                
                #elif line[0:5] == "Chain" or line[0:11] == "Heavy Chain" or line[0:11] == "Light Chain": # Start of a sequence block 
                
                elif re.search(r'^(Heavy\s|Light\s)?Chain[:\[]', line):
                        #remove-colon-from-end-of-line;
                        key = line.strip(':')
                        dic[key] = ''     # Initialize data storage 
        
                        inSequence = True
        
                elif inSequence:    # We are within a sequence block
    
                        #cleanup(line):      
                        # Strip whitespace and return character
                        line = line.replace(' ', '')
                        line = re.sub(r'\d', '', line)
        
                        dic[key] += line  # Append sequence information to the data

                else:                # Normal line
                        if(len(line) > 1):
                                (key, value) = line.split(':', 1)
                                value = re.sub(r'^\s+', '', value)
                                
                                # Special case of note records where we add '-' and the previous line's key
                                if key[0:4] == 'Note':
                                        key += "-" + previousKey
                                        dic[key] = value
                                        continue
                                previousKey = key     # Update the previous key to be the key from this line

                                dic[key] = value 
        print(json.dumps(dic, indent=2))

