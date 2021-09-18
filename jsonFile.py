import json

# Function to open the JSON file
def jsonFileOpen(filename):
    f = open(filename)
    data = json.load(f)
    return data