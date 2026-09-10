import numpy as np

v=np.zeros(12)
print(v)

v[5]=1
print("print f with 1 step :",v)

v[2]=2
print("with 2 step",v)
print()

# creat a vector with values ranging from 10 to 100
v=np.arange(0,100)
print("print 0 to 100 : ",v)
print()


#creating 2D array
v=np.arange(10,19).reshape(3,3)
print("2D array :",v)
print()

#to generate identity method 
v= np.eye(3)
print("Identity matrix :",v)
print()

#Creating a random matrix in 3x3x3
v= np.random.random((3,3,3))
print("Random matrix :",v)
print()

#to creat a 5x5 array with random values
v= np.random.random((5,5))
dmix,dmax=v.min(),v.max()
print("Min and max ",dmix,dmax)
print()







#creat an array of 20 zeros 
z=np.zeros(20)
print("print 20 zeros : ",z,"\n")

#creat an array of 15 one 
a= np.ones(15)
print("creat 15 one ",a,"\n")

#crea array of ten 5
b= np.ones(10)
c=b*5
print("creat 5 ten times :",c,"\n")

#creat an array of even integers from 5 to 90
even = np.arange(6, 91, 2)
print("Even number between 6 to 98 :",even,"\n")

#creat an identity matrix of 7x7
i = np.eye(7)
print("Identity matrix of 7x7 :",i,"\n")

# # #generate a number of an array of 30 random sample from a standard which range is 0-1
r = np.random.uniform(0,1,30)
print("print 30 random sample between 1-20 :",r,"\n")

r = np.random.normal(0,1,30)
print(r,"\n")

#creat an array using numpy and perform slicing 
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(arr[2:6],"\n")
print(arr[:6] ,"\n")


arr1 = np.random.randint(1,20,30)
print(arr1,"\n")
print(arr1[3:7])









