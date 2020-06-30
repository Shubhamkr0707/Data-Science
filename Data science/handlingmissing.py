import pandas as pd 
import numpy as np 
file_csv=r"C:\Users\Shubham\Downloads\py-master\py-master\pandas\5_handling_missing_data_fillna_dropna_interpolate\weather_data.csv"
# df=pd.read_csv(file_csv)
# print(df)
df=pd.read_csv(file_csv,parse_dates=["day"])
# print(df)
# filling_values=df.fillna({'temperature':0,
#                           'windspeed':0,
#                           'event':"Noevent"})
# print(filling_values)
# filling_values=df.fillna(method="ffill")
# print(filling_values)
# filling_values=df.fillna(method='bfill',limit=1)
# print(filling_values)

# interpolate_values=df.interpolate()
# print(interpolate_values)
# interpolate_values=df.interpolate(method="time")
# print(interpolate_values)

droping_values=df.dropna()
print(droping_values)
droping_values=df.dropna(how='all')
print(droping_values)
droping_values=df.dropna(thresh=1)
print(droping_values)