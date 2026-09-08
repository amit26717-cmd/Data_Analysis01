import pandas as pd 
df=pd.read_csv('orders.csv')
df.head()
# # print(df)
# df.info()
# # df.columns[2]
# # print(df['Class'])
# df = pd.read_csv('t.csv', sep=';')
# print(df)

# print(df.loc[15])
# print(df.iloc[0,'word_freq_all'])

pr=df[(df['Category']=="Electronics")&(df["Country"]=="Japan")&(df["Product"]=="Mouse")]
print(pr)
#