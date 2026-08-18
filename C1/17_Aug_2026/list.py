list = [10,'Amit',51]
print(type(list).__name__)
print(list)

list1 =[10,'a','b',20,30,40]


print(list1[1:5])
print(list1[2:])
print(list1[:5])

for i in list1 :
    print(i)

# for i in list1 :

print(list1[::-1])
list1[2]="RAm"
print(list1)
a = eval(input("Enter List :- "))
list2 = [a]
print(list2)

a = str(input("Enter List :- "))
list3 =[a]
print(list3)

l= list(range(5,55,5))
print(f"The list is :- {l}")

s="Symbi"
l = list(s)
print(l)

s = 'Learning Python is very easy'
l=s.split()
print(l)

# nested list

n =[10,20,[30,40],["Amit ",'patel',51]]
print(n)
print(n[0])
print(n[2])
print(n[2][1])
print(n[3][2])
a = int(input("Enter the index :- "))
print(n[a])

# nested List as Matrix

n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)

print('Element Row Wise ')
for r in n :
    print(r)

print('Element by Matrix Wise ')
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j], end = " ")
    print()

# list comprihensive
s= [x*x for x in range (1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m= [x for x in s if x%2==0]
print(m)


