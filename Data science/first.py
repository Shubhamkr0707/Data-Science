import pandas as pd 
laptop={"Brand":["Hp","Lenovo","Dell","Apple","Samsung","Acer"],
        "Price":[32000,33000,34000,32000,33000,35000],
        "Model":[2013,2015,2016,2020,2020,2020],
        "Stock":["In","Out","In","In","Out","Out"],
        "Seller":["Online","Online","Online","Offline","Offline","Online"],
        "Supplier":["Amazon","Flipkart","Shopclues","Flipkart","Crown","Zest"],
        "Ratings":["4star","5star","3star","5star","3star","2star"]}
df=pd.DataFrame(laptop)
# print(df)
# print(df.head(2))
x=df[df["Model"]>2015][df["Price"]>33000][df["Seller"]=="Online"][df["Stock"]=="In"]
# print(x)
# y=df["Price"].max()
# print(y)
# z=df[df.Price==df.Price.max()]
# For column name containing space
# z=df[df["Price"]==df["Price"].max()]
# print(z)
# i=df.set_index("Brand",inplace=True)
# print(i)
# print(df)
r=df.reset_index(inplace=True)
print(r)   
print(df)