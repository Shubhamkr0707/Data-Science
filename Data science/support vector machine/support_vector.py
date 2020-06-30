import pandas as pd
import numpy as np 
from sklearn.datasets import load_iris
iris=load_iris()
# print(dir(iris))
df=pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.head())
df['target']=iris.target
# print(df.head())
# print(iris.target_names)
# print(df[df.target==1].head())
df['flower_name']=df.target.apply(lambda x:iris.target_names[x])
# print(df.head())
from matplotlib import pyplot as plt 
df0=df[df.target==0]
df1=df[df.target==1]
df2=df[df.target==2]
# plt.xlabel("sepal length (cm)")
# plt.ylabel("sepal width (cm)")
# plt.scatter(df0["sepal length (cm)"],df0["sepal width (cm)"],color='green',marker="+")
# plt.scatter(df1["sepal length (cm)"],df1["sepal width (cm)"],color='blue',marker=".")
# plt.show( )
# plt.xlabel("petal length (cm)")
# plt.ylabel("petal width (cm)")
# plt.scatter(df0["petal length (cm)"],df0["petal width (cm)"],color='green',marker="+")
# plt.scatter(df1["petal length (cm)"],df1["petal width (cm)"],color='blue',marker=".")
# plt.show()
from sklearn.model_selection import train_test_split
x=df.drop(['target','flower_name'],axis="columns")
y=df.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.svm import SVC
model=SVC()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))