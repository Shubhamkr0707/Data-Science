import pandas as pd 
import numpy as np 
file_csv=r"C:\Users\Shubham\Downloads\nyc_weather.csv"
df=pd.read_csv(file_csv)
# print maximum temperature and minimum temperature
maxx=df["Temperature"].max()
print(maxx)
minn=df["Temperature"].min()
print(minn)

# Which dates its rain and print dates

rain=df["EST"][df["Events"]=="Rain"]
print(rain)

# What is average wind speed and we have to find mean

averageee=df["WindSpeedMPH"].mean()
print(averageee)

# flil missing values to Zero
fill_naaaa=df.fillna(0)
print(fill_naaaa)



# Next video Tutorial 2
 