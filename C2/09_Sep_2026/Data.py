import pandas as pd 
df=pd.read_csv('orders.csv')

ch= df[~df["Country"].isin(["USA","Sweden","Brazil","India"])]
# print(ch)


df.rename(columns={"OrderID": "Order ID"}, inplace=True)
print(df.columns)

print(df.head())


