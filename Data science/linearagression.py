import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
area_price={"area":[2600,3000,3200,3600,4000],
            "price":[550000,565000,610000,680000,725000]}
df=pd.DataFrame(area_price)
# print(df)

# plt.scatter(df.area,df.price)
# plt.show()
reg=linear_model.LinearRegression()
x=reg.fit(df[['area']],df.price)
# print(x)
# m=reg.predict([[5000]])
# print(m)
# z=reg.intercept_
# y=reg.coef_
# print(y)
# print(z)


# price_area={"area":[1000,2000,3000,4000,500,4500]}
# df1=pd.DataFrame(price_area)
# # print(df1)
# p=reg.predict(df1)
# df1['prices']=p
# print(df1)

# plt.scatter(df.area,df.price)
# plt.plot(df.area,reg.predict(df[['area']]))
# plt.show()

# 20th April 2020
# EXporting csv file and importing price of csv
df2=pd.read_csv(r'D:\work\Data science\areas.csv')
p=reg.predict(df2)
df2["prices"]=p
df2.to_csv('prediction.csv',index=False)
