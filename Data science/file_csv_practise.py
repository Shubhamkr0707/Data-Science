import pandas as pd 
import numpy as np 
file_csv=r"D:\work\Data science\first.csv"
# df=pd.read_csv(file_csv,skiprows=1)
# print(df)
# if header is not then
# df=pd.read_csv(file_csv,header=None,names=["ticker","eps","revenue","price","people"])
# print(df)
# for reading particular rows
df=pd.read_csv(file_csv,nrows=3)
print(df)