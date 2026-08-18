# tuple declaration
a = 30,40,50,'amit', .08
print(a)
print(type(a).__name__)

#using tuple function
d = tuple(range(2,60,3))
print(d)
print(type(d).__name__)
print(d[::-1])

#concotanation of tuples
m = 10,50,30,10
n= 14,45,12
print(m.index(10))
v=m+n
print(v)
print(len(v))
#count function with tuple
print(v.count(10))
g=m*4
print(g)

num = 10,50,30,46,74,25,11,50
num2= 4,785,7,854,78,47
print(num.index(50))
print(num)
print(sorted(num))
print(reversed(num))
print(min(num))
print(max(num))
# print(cmp(num,num2))



