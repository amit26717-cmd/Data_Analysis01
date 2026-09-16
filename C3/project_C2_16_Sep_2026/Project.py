import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("superstore_excel-selected-columns.csv")

print(df.head())
print(df.shape)
print(df.columns)

df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df.isnull().sum())
print(df.duplicated().sum())

cat_count = df["Category"].value_counts()
print(cat_count)

region_count = df["Region"].value_counts()
print(region_count)

df["Month"] = df["Order Date"].dt.month
month_count = df["Month"].value_counts().sort_index()
print(month_count)

cust_orders = df["Customer ID"].value_counts()

total = 0
for i in cust_orders:
    total += i
avg = total / len(cust_orders)
print("avg orders per customer =", avg)

labels = []
for i in cust_orders:
    if i == 1:
        labels.append("Low")
    else:
        labels.append("High")

print(labels[:5])

plt.bar(cat_count.index, cat_count.values)
plt.title("Orders by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

plt.plot(month_count.index, month_count.values)
plt.title("Orders by Month")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.show()

plt.hist(cust_orders)
plt.title("Orders per Customer")
plt.show()