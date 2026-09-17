import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("superstore_excel-selected-columns.csv")


print(df)
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.shape)
print(df.shape[0])
print(df.shape[1])
print(df.columns)
print(df.isnull().sum)
print(df.duplicated())
print(df["Ship Mode"].value_counts())
print(df["Segment"].value_counts())
print(df["Category"].value_counts().head(10))
print(df["Sub-Category"].value_counts().head(10))

df["Order Date"] = pd.to_datetime(df["Order Date"],errors="coerce")
od_year=df["Order Date"].dt.year.dropna().to_numpy() 
print(od_year)

print(np.mean(od_year))
print(np.min(od_year))
print(np.max(od_year))
print(np.std(od_year))
print(df["Order Date"].isna().sum())

df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print((df[["Order Date", "Ship Date", "Order Year", "Order Month", "Shipping Days"]].head()))