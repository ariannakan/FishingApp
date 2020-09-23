import requests
import json
import datetime
import time
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import os
import sys
import urllib3

urllib3.disable_warnings()


mytoken = 'XOezwYtXYrtbigFFqCHvXDkaXRUwYYgT'


#base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
base_url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter'

header = {'token' : mytoken}


service_call = '/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20200901&end_date=20200930&datum=MLLW&station=9414131&time_zone=lst_ldt&units=english&interval=hilo&format=json'

# Use the same begin and end date for just one day's data. Format for the API request
begin_date = datetime.datetime.now().strftime("%Y%m%d")
end_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y%m%d")

#range = 730 #number hours in a month

# Pillar Point


def GETrequest(obj):
    startTime=time.time()
    #if header != '': print(header)
    if 'params' in obj:
        response = requests.get(obj['url'], headers=obj['headers'], params=obj['params'], verify=False)
    else:
        response = requests.get(obj['url'], headers=obj['headers'], verify=False)
    response.content
    #print(response.url)
    durationTime=time.time() - startTime
    try:
        response.json()
        #print(str(response.status_code)+"|"+str(durationTime)+"|"+response.text+"\n")
        return response
    except ValueError: #no JSON returned
        #print(str(response.status_code)+"|"+str(durationTime)+"\n")
        return response




PillarPoint = {
    'url':base_url,
    'headers':'',
    'params': {
        'station': '9414131',  
        'product':'predictions',
        'begin_date': begin_date,
        'end_date': end_date,
        'time_zone': 'lst_ldt',
        'units': 'english',
        'interval': 'hilo',
        'datum':'MLLW',
        'format': 'json'
    }
}



response = GETrequest(PillarPoint)
r = response.json()

# Define my pandas Dataframe with the columns that I want to get from the json
response_data = pd.DataFrame.from_dict(r['predictions'], orient='columns')
print(response_data)

'''
for prediction in response["predictions"]:
    time = prediction['t']
    level = prediction['v']
    # push a list of data into a pandas Dataframe at row given by 'index'
	response_data.to_json()
    
'''