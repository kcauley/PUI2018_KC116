import os
import json
import pprint
import csv
import sys
import pandas as pd 
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib

# Accept arguments

# MTA API Key
api_key=sys.argv[1]

# Bus line
# Example: B52 or B69
bus_line=sys.argv[2]

# Build a string that is the MTA URL / API endpoint that we will be interacting with
# Example of formatted string: http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=b1a1a460-c03c-41c5-b294-3cad9d880de6&VehicleMonitoringDetailLevel=calls&LineRef=B52
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line 
print(url)

# Make web request with the URL from above
# Response comes back as data that must be decoded
# response = what we get back from the url
response = urllib.urlopen(url)

# Decode the data here into something human readable
# data = response decode as utf-8

data = response.read().decode("utf-8")

# Convert the response into a (JSON) dictionary 
# data = the decoded response as a dictionary
dataDict = json.loads(data)

# Extract the array of vehicle activity located at dataDict -> Siri -> ServiceDelivery -> VehicleMonitoringDelivery -> First object -> VehicleActivity
vehicleActivities = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# Loop through the array of activities and write a summary to busline.csv
index = 0 
file = open('busline.csv', 'w+')
for activity in vehicleActivities:  
    # Extract the journey data from the activity and format it into a string
    journey=activity['MonitoredVehicleJourney']
    s='Bus %s is at Latitude:%s and Longitude:%s' % (str(index), str(journey['VehicleLocation']['Latitude']), str(journey['VehicleLocation']['Longitude']))
    # Write the newly formatted string to file
    file.write(s+'\n')
    index+=1

# Stop editing busline.csv
file.close()


# Repeat the above 
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

vehicleActivities = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

index = 0
df_all=pd.DataFrame(columns=['latitude','Longitude','Busstop','Stopstatus'])
for activity in vehicleActivities:
    journey = activity['MonitoredVehicleJourney']
    latitude = journey['VehicleLocation']['Latitude']
    longitude = journey['VehicleLocation']['Longitude']
    if len(journey['OnwardCalls']) < 1:
        busStop='N/A'
        stopStatus='N/A'
    else:
        busStop = journey['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopStatus= journey['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    index+=1 
    df_all.loc[index] = [latitude,longitude,busStop,stopStatus]
    print (latitude,longitude,busStop,stopStatus)
df_all.to_csv('bustime.csv')
