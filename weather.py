
'''Javascript Object Notation'''
# Every language now has libraries for parsing and generating JSON data.

import json
from pprint import pprint
# Defined a multi-line string.
people_string = '''         
{
    "people": [
        {
            "name": "John Smith",
            "phone": "617-785-0000",
            "emails": ["garv@bogusemail.com", "chawla@bogusemail.com"],
            "has_license": false
        },
        {
            "name": "Garv Chawla",
            "phone": "617-785-7082",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

'''
It looks like a Dictionary. It has a key called "people". 
The value of "people" is an array of more objects. Here 2 more object.
And each object has a key of name, phone, emails, has_license
'''


# print(people_string)
# Now, load it to a python object to work better.
# To load it into Python from a string use --> json.loads()

data = json.loads(people_string)
print(type(data))           # <class 'dict'>

"""
JSON	        Python
object	        dict
array	        list
string	        str
number(int)	    int
number(real)	float
true	        True
false	        False
null	        None
"""

pprint(data)

for person in data['people']:
    print(person)

# {'name': 'John Smith', 'phone': '617-785-0000', 'emails': ['garv@bogusemail.com', 'chawla@bogusemail.com'], 'has_license': False}
# {'name': 'Garv Chawla', 'phone': '617-785-7082', 'emails': None, 'has_license': True}

for person in data['people']:
    print(person['name'])

# John Smith
# Garv Chawla

# Now, doing reverse ie to dump the python object to a JSON string. Use json.dumps() method.

for person in data['people']:
    del person['phone']         # This will delete the phone key and the value.

# dump this new without phone data, into a string.

new_string = json.dumps(data)
print(new_string)
# {"people": [{"name": "John Smith", "emails": ["garv@bogusemail.com", "chawla@bogusemail.com"], "has_license": false}, {"name": "Garv Chawla", "emails": null, "has_license": true}]}

# to make the string look better, pass in indent = 2.

new_string = json.dumps(data, indent=2)
print(new_string)

new_string = json.dumps(data, indent=2, sort_keys=True)     # emails then has_license, then name
print(new_string)





'''
import requests
from pprint import pprint

def main():
    city = input("Enter a City\n")
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=33cfcb7b14b093a38a3f100285722e49&units=metric")
    weather = response.json()
    pprint(weather)
    print("The weather for", weather['name'], end=" ")
    pprint(weather['main']['temp'])  # we have a key called main. # inside that key - main, we have another dictionary with a key - temp.
    # We have a dictionary with a key called main and inside that we have  another dictionary with a key called main.

    # What if i need the description to be shown. Here it's 'mist'.
    # We have a Dictionary inside which we have a key - 'weather'. That key has a List with just 1 item [].
    # That list inside the key has another Dictionary with a key called 'description'.

    pprint(weather['weather'][0]['description'])
    # Dictionary Called weather.
    # Inside that we have a key called Weather
    # Inside that key, we have a list with 1 item. We need 0th Item.
    # Inside that we have a dictionary and we need the key - description. - which has a value called - 'moderate rain'.


if __name__ == '__main__':
    main()
'''

'''
import urllib.parse
import requests
from pprint import pprint

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'lhr'

url = main_api + urllib.parse.urlencode({'address':address})

json_data = requests.get(url).json()

pprint(json_data)

'''
