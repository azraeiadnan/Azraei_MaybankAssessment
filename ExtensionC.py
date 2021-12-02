#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
#Weather and City
url = "http://api.open-notify.org/iss-now.json"
df = pd.read_json(url)
df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc[ 'longitude','iss_position']
df.reset_index(inplace=True)

weather_base = "http://api.weatherapi.com/v1/current.json?key="
weather_key = "655e7f09794147e694e121906213011&q="
x = df.latitude
y = df.longitude
queryX = str (x[0])
queryY = str (y[0])

allTogether = weather_base+weather_key+queryX+","+queryY

print("lat = " +queryX)
print("lon = " +queryY)

wf = pd.read_json(allTogether)
print(wf)

import requests
r = requests.get(url='http://api.open-notify.org/astros.json')
r.json()


# In[ ]:




