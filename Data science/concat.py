import pandas as pd 
import numpy as np
india_weather={"City":["Mumbai","Delhi","Bangalore"],
              "temperature":[32,30,40],
              "humditiy":[80,70,62]   

}
df1=pd.DataFrame(india_weather)
# print(df1)
us_weather={"City":["newyork","chicago","losvegas"],
              "temperature":[12,40,23],
              "humditiy":[40,90,62]   

}
df2=pd.DataFrame(us_weather)
# print(df2)

# Starting of concat of values

# concat_values=pd.concat([df1,df2],ignore_index=True)
# print(concat_values)

concat_values=pd.concat([df1,df2],keys=["india","usa"])
# print(concat_values)

# Suppose we want data by location
# location_values=concat_values.loc['india']
# print(location_values)
# location_values=concat_values.loc["usa"]
# print(location_values)

temperature={""}