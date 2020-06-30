import pandas as pd 
import numpy as np 
from sklearn import linear_model
df=pd.read_csv(r"homeprices.csv")
z=df.bedrooms.median()
#print(z)
df.bedrooms=df.bedrooms.fillna(z)
# print(df)
reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)
c=reg.coef_
print(c)
i=reg.intercept_
print(i)
p=reg.predict([[3000,3,40]])
print(p)