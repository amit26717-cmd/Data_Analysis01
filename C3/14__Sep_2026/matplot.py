import matplotlib.pyplot as plt
import numpy as np
# x = [10,15,20,25,30,35,40,45,50]
# y = [1000,2000,3000,4000,5000,6000,7000,8000,9000]

# plt.plot(x,y)       # print the line graph 
# print(plt.show())   # to show the any types of graph

# plt.xlabel("X axis")
# plt.ylabel("Y axis ")
# plt.title("First graph")

# # this is print Bar graph 
# b=plt.bar(x,y)       
# print(b)


# #this print the point
# s=plt.scatter(x,y)             
# print(s)


# plt.figure(figsize=(8,5))
# plt.plot(x,y ,color ='red',marker = 'o',linestyle = '--',linewidth = 2 , markersize = 8,markerfacecolor = 'green')
# plt.title("Comparison of age Vs salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# print(plt.show())



# # That line prints the multiple lines 
# x = [1,3,4,5,6,7,8,10,12]
# y1 = [1000,2000,3000,4000,5000,6000,7000,8500,9000]
# y2 = [3000,5000,7000,4000,6000,12000,7000,8000,9500]
# y3 = [2000,3000,8000,6000,5000,9000,7000,8000,10500]

# plt.plot(x,y1,label='1st 4  months profit')
# plt.plot(x,y2,label='2nd 4 months profit')
# plt.plot(x,y3,label='3rd 4 months profit')

# plt.title("Comparison of sales and profit ")
# plt.xlabel("Months")
# plt.ylabel("quaters sales Profits")
# plt.legend()
# print(plt.show())




# print the data set using  graphs 
x =np.array([1,3,4,5,6,7,8,10,12])
y1 = [1000,2000,3000,4000,5000,6000,7000,8000,9000]
y2 = [3000,5000,7000,4000,6000,12000,7000,8000,9000]
y3 = [2000,3000,8000,6000,5000,9000,7000,8000,10000]
plt.figure(figsize=(8,5))
width = 0.2
plt.bar(x - width, y1, width=width,label='1st 4  months profit')
plt.bar(x , y2, width = width ,label='2nd 4 months profit')
plt.bar(x + width, y3, width=width,label='3rd 4 months profit')

plt.title("Comparison of sales and profit ")
plt.xlabel("Months")
plt.ylabel("quaters sales Profits")
plt.legend()
plt.show()
