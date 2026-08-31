details = { 51 : 'Amit patel ',
           70 : 'Ayush',
           87 : 'Himesh',
           35 : 'Abhishek'
        }
print(details)

#print using Pairs Values

print(details[51])
print(details[35])
print(details[70])

# element of dictionry using user input

name={}
e = int(input("Give the no of students : "))
i = 1
while i<=e :
    names = input("Students name : ")
    marks = int(input("Enter marks : "))
    i = i+1
print("Name of students ","\t","marks")
for x in name:
    print("\t",x,"\t\t",name[x])
