def table(number):
   
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")


times = int(input("Enter your choice how many table you want to print "))
i =1
while i<times+1:
    n = int(input("Enter your Number : "))
    table(n)
    print()
    i+=1