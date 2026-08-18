#input tuples element an print their sum and averages

tup=eval(input("enter your number  :- "))
sum=0
print(tup)
for i in tup:
    
    sum+=i
print("the sum of tuple is :- ",sum)
print("The Avarage of tuple is :- ",sum/len(tup))
print(type(tup))



