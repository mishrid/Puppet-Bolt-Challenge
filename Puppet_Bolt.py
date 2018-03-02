import json
import sys

jsonData = sys.stdin.read()

#ensure file is not empty
if len(jsonData) == 0:
	print("There is no data in json file")
	sys.exit(0)

def json_writer(jsonData):
    
    #load contents of json file to Python Dictionary structure
    jsontoPython = json.loads(jsonData)

    #initialize empty dictionary to store new dictionary structure
    pythonDictionary = {}

    #iterate through every node in json file, adding to pythonDictionary where top level keys are the keys present in the results,
    #the value of each is a dictionary mapping the different values present to the results to an array of nodes with those values.

    for key in jsontoPython:
        node_dictionary = jsontoPython[key]
        for specific_key in node_dictionary:
            if specific_key not in pythonDictionary:
                pythonDictionary[specific_key] = {node_dictionary[specific_key]: [key]}
            else:
                if node_dictionary[specific_key] in pythonDictionary[specific_key]:
                    pythonDictionary[specific_key][node_dictionary[specific_key]] = pythonDictionary[specific_key][node_dictionary[specific_key]] + [key]
                else:
                    pythonDictionary[specific_key][node_dictionary[specific_key]] = [key]


    #write contents of python dictionary to sys.STDOUT and format in a readable way
    json.dump(pythonDictionary,sys.stdout, indent=4)
  

json_writer(jsonData)