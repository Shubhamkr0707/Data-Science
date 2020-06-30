import pandas as pd 
import numpy as np 
file_csv=r"C:\Users\Shubham\Downloads\world-happiness\2019.csv"
df=pd.read_csv(file_csv)
x=df.groupby("Score")
print(x)

# First Question find top 5
# first=df.head()
# print(first)

# # second Question find top 5
# second=df.tail()
# print(second)

# # third Question columns name

# third=df.columns
# print(third)


# # fourth Question row index and meta infromation
# fourth=df.index
# print(fourth)
# fourth=df.info
# print(fourth)
# # fifth find happiness from 5th to 10th
# fifth=df.iloc[4:10]
# print(fifth)

# #sixth change index column
# sixth=pd.read_csv(r"C:\Users\Shubham\Downloads\world-happiness\2019.csv",index_col="Country or region")
# print(sixth)

# # findingcountry and region by ranking
# seventh=sixth.loc[["Japan","India","Pakistan"],"Overall rank"]
# print(seventh)