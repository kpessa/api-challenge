from City import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from IPython.display import JSON
from scipy.stats import linregress


# Import API key
from api_keys import weather_api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# Generate Cities List
# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print("Length of cities: ", len(cities))

df_row = 0
# Set up dataframe to accept cities
df = pd.DataFrame([],columns=["City","Lat","Lon","Max Temp","Humidity","Cloudiness","Wind Speed", "Country", "Date"])

print("-----------------------------")
print("Beginning Data Retrieval")
print("-----------------------------")
record = 1
set_ = 1

for city_name in cities:
    city = City(city_name)
    if city.skipQ():
        print("City not found. Skipping...")
    else:
        print(f"Processing Record {record} of Set {set_} | {city.name}")
        # add information to dataframe and then increase row
        
        df.loc[df_row,"City"] = city.name
        df.loc[df_row,"Lat"] = city.lat
        df.loc[df_row,"Lon"] = city.lng
        df.loc[df_row,"Max Temp"] = city.max_temp
        df.loc[df_row,"Humidity"] = city.humidity
        df.loc[df_row,"Cloudiness"] = city.cloudiness
        df.loc[df_row,"Wind Speed"] = city.wind_speed
        df.loc[df_row,"Country"] = city.country
        df.loc[df_row,"Date"] = city.date

        df_row += 1
        record += 1
        if record > 50:
            set_ += 1
            record = 1

print("-----------------------------")
print("Data Retrieval Complete")
print("-----------------------------")

df.to_csv(output_data_file)

print(df)