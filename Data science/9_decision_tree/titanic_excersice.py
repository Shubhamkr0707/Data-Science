import pandas as pd 
import numpy as np 
df=pd.read_csv(r"D:\work\Data science\9_decision_tree\Exercise\titanic.csv")
# print(df.head())
# df.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked"],axis='columns')
# print(inputs.head())
inputs=df.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked",'Survived'],axis="columns")
# print(inputs.head())
target=df.Survived
# print(target)
inputs.Sex=inputs.Sex.map({"male":1,"female":2})
# print(inputs.Age[:10])
inputs.Age=inputs.Age.fillna(inputs.Age.mean())
# print(inputs.Age[:10])
# print(inputs)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(inputs,target,test_size=0.2)
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))