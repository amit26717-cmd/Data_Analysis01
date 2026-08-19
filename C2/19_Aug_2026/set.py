#understanding of set 


s = { 50,60,70,'hi','nghg'}
print(s)
print(type(s).__name__)
a= set(s)
print("the primary set element is :",a)
n=int(input("enter the number to add :-"))
a.add(n)
print("the set after new element added :- ",a)

#updating set element 

h = {10,15,"university","area",35,40,45}
print("element of h :",h)

b= [20,25,30]
print("element of b :",b)
h.update(b[:2])
print("element of h after updation :",h)

# pop() operation on set 

j={40,50,78,45,"amit"}
print("Element of j : ",j)
print(j.pop())
print("element of j after pop operation : ",j)

#remove () operation on set

k={10,45,"amit",98,45,67}
print("Element of k : ")
k.remove(10)
print("Element of k after remove opration :- ",k)

# union (|) af set 
u= {10,58,45,65,21}
print("Element of u :",u)
y={4,6,7,8,1,2,0}
print("Element of y :",y)
#print(u.union(y))
print("element after union : ",u|y)

#Finding element using membership operator

t=set("This is the Data Analyst class ")
print("Element of t : ",t)
print('t' in t)
print('o'not in t)



