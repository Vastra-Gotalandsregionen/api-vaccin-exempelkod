# coding: utf-8
"""
Fetching all testcenters and filtering those having available timeslots
"""

# import requests
import json

# uncomment when the API is up and running again
"""
headers = {
    'client_id':'c4d279f9b8094dbaafd0162c5a606623', 
    'client_secret': '39D6cAB5D89c448ea3355aAC61De19e7'
}

req = requests.get('https://test.api.vgregion.se/e-crm-scheduling-public/api/v1/testCenter', headers = headers)
data = json.load(req.text)

testcenters = data['testcenters']

# Print the data of dictionary
# print("\ntestcenters:", testcenters)

# print(len(testcenters), 'testcenter')

for testcenter in testcenters:
    if testcenter['timeslots'] != 0 and testcenter['timeslots'] != None:
        print('{0} har {1} st lediga tider - boka här {2}'.format(testcenter['title'], testcenter['timeslots'], testcenter['urlBooking']))
"""
  
# Opening JSON file
with open('../sample-data/vaccine-2021-05-25.json') as json_file:
    data = json.load(json_file)
    
    testcenters = data['testcenters']
  
    # Print the data of dictionary
    # print("\ntestcenters:", testcenters)

    # print(len(testcenters), 'testcenter')
    
    for testcenter in testcenters:
        if testcenter['timeslots'] != 0 and testcenter['timeslots'] != None:
            print('{0} har {1} st lediga tider - boka här {2}'.format(testcenter['title'], testcenter['timeslots'], testcenter['urlBooking']))