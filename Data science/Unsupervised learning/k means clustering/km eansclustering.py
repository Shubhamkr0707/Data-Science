import pandas as pd 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt 
df=pd.read_csv(r"D:\work\Data science\Unsupervised learning\k means clustering\income.csv")
# print(df.head())
plt.scatter(df["Age"],df["Income($)"])
# plt.show()
km=KMeans(n_clusters=3)
y_predictedd=km.fit_predict(df[["Age","Income($)"]])
# print(y_predictedd)
df['cluster']=y_predictedd
# print(km.cluster_centers_)
# print(df.head())
df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()
# plt.show()


# Using Min Max scaler to fit values
scaler=MinMaxScaler()
scaler.fit(df[["Income($)"]])
df["Income($)"]=scaler.transform(df["Income($)"])
scaler.fit(df.Age)
df.Age=scaler.transform(df.Age)
# print(df)
km=KMeans(n_clusters=3)
y_predictedd=km.fit_predict(df[["Age","Income($)"]])
# print(y_predictedd)
df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
# plt.scatter(km.cluster_centers_[:,1],color='purple',marker="*",label='centroid')
# plt.xlabel('Age')
# plt.ylabel('Income($)')
# plt.legend()
# plt.show()
k_rng=range(1,10)
sse=[]
for k in k_rng:
    km=KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)
    print(sse)
plt.xlabel('k')
plt.ylabel("SSE")
plt.plot(k_rng,sse)
plt.show()