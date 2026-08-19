# program to print different vovels present in the given word 

w= input("Enter the word /sentence ")
t =set(w)
v= { 'a','e','i','o','u'}

a=t.intersection(v)
print("The vovel found in the given word ",w,"are",a)
