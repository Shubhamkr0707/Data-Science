import pandas as pd
import numpy as np 
df=pd.read_csv("D:\work\Data science\logistic regression\insurance_data.csv")
# print(df)
from matplotlib import pyplot as plt
plt.scatter(df.age,df.bought_insurance,marker="+",color='red')
# plt.show()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance,test_size=0.1,random_state=10)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(x_test)
z=model.score(x_test,y_test)
print(z)

# Logistic regression multi class classification
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
d=load_digits()
# print(digits.data[0])
# plt.gray()
# for i in range(5):
#  plt.matshow(digits.images[i])
# plt.show()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
s=model.score(x_test,y_test)
print(s)
print(model.predict([d.data[67]]))
print(model.predict(d.data[0:6]))