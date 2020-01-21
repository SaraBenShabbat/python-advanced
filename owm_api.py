#!/usr/bin/env python3.8.0

import argparse
import requests
import sys
import json
import pprint

parser = argparse.ArgumentParser()

# A positional argument, by default every argument is mendatory.
parser.add_argument('zip', type = str, help = 'Enter the zip code of the location - you wanna get the weather info.')

# An optional argumentm as I have a default val; In addition due to the fact 
# that I signed it with minus sign, because of it when I run the script - I have# to mention the name of the flag ('--conutry' or '-c') and afterwards the val.
parser.add_argument('--country', '-c', type = str, default = 'us', help = 'Enter the country name of the loaction - you wanna get the weather info.')    

args = parser.parse_args()


response = requests.get('https://samples.openweathermap.org/data/2.5/weather?zip=' + str(args.zip) + ',' + str(args.country) + '&appid=b73bbd6c6c33d3a60422ca5069912942')


if response.status_code != 200:
    print('Error')
    sys.exit(1)    
print('response.text =\n' + str(response.json()))




"""
In order the user to see the help text, he has enter '<desired interpreter> 
<desired file to run> --help/-h'
"""


"""
print('args.zip = ' + args.zip)
print('args.country = ' + args.country)
"""


"""
print('response.status_code = ' + str(response.status_code))
print('response.headers = ' + str(response.headers))
print('response.headers["Content-Type"] = ' + str(response.headers['Content-Type']))
"""


"""
json_formatted = json.loads(response.text)
pprint.pprint(json_formatted)
"""


"""
print("\n".join("{}\t{}".format(k, v) for k, v in json_formatted.items()))
"""


