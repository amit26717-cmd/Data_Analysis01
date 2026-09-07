
# #panadas program to print marks of subjects 
import pandas as pd
# marks= pd.Series([10,20,30,40],index = ['Maths', 'Computer Network','DBMS','Computer Fundamental'])

# print(marks)

# #Details 

# data={
#     'Name':['   Amit','Himesh ','Ayush','Noor'],
#     'Age':[20,20,22,20],
#     'city':['Jaunpur','Jaunpur','Varanashi','Badagav'],
#     'Desiganation':['Data analyst ','Spring Boot','Data analyst ','Mern']
# }
# df=pd.DataFrame(data)
# # df.index=range(1,len(df)+1)
# df.index=df.index+2
# print(df)
# print(df.index)

# '''
# 0   +2
# 1   +2  
# 2   +2
# 3   +2

# '''


# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)



df=pd.read_csv('t.csv')
df.head()
# print(df.to_string(index=False))

