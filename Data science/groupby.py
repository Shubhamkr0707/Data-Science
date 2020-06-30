import pandas as pd 
import numpy as np 
file_csv=r"C:\Users\Shubham\Downloads\py-master\py-master\pandas\7_group_by\weather_by_cities.csv"
df=pd.read_csv(file_csv)
g=df.groupby('city')
# print(g)
# for city,city_df in g:
#     print(city)
#     print(city_df)
# single=g.get_group('new york')
# print(single)
max_temp=g.max()
print(max_temp)
