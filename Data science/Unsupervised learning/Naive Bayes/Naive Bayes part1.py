import pandas as pd 
import numpy as np 
df=pd.read_csv(r"D:\work\Data science\Unsupervised learning\Naive Bayes\titanic.csv")
# print(df.head())
df.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked"],axis='columns',inplace=True)
# print(df.head())
target=df.Survived
inputs=df.drop("Survived",axis='columns')
dummies=pd.get_dummies(inputs.Sex)
inputs=pd.concat([inputs,dummies],axis='columns')
# print(inputs.head(3))
inputs.drop("Sex",axis='columns',inplace=True)

# To check Any columns has Null Vale
print(inputs.columns[inputs.isna().any()])

# To fill Nan Values in Age
inputs.Age=inputs.Age.fillna(inputs.Age.mean())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(inputs,target,test_size=0.2)
print(len(x_train))
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))
print(y_test) 