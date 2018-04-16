
'''
How to write JSON files into Python objects and then write those objects back to JSON files.
'''

import json
from pprint import pprint

# To load a file use json.load() method.
# json.loads() is used when we load from a string.
# open the file states.json in the same directory using -> with open('states.json')

with open('states.json') as f:
    # Now, time to load in that file
    data = json.load(f) # load in the file 'f'.


# There's a 'state' key and that has a list of Objects. And these objects have a 'name', 'abbreviation', 'area_codes'.
for state in data['states']:
    print(state)

for state in data['states']:
    print(state['name'], state['abbreviation'])

# Now, let's remove one of the area codes and then write that back into the file.

for state in data['states']:
    del state['area_codes']

print(data['states'])

# Now, we have to write this file into JSON.
# The dump() method converts the data into a JSON file, while dumps() method converts the data to a JSON string.

# open the file
with open('new_states1.json', 'w') as f:
     json.dump(data, f)     # We want to dump the data we have ie 'data' to the file we opened 'f'.

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)  # We want to dump the data we have ie 'data' to the file we opened 'f'.


