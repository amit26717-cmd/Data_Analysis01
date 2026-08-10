num = int(input("Enter the number you want to cheak :- "))

if num<2:
    print ("Invailid input")
else :
    prime = True 
    for i in range(2,num) :    
        if num%i==0:
            prime = False
            break

    if prime == True :
        print ("prime")
    else:
        print("not prime")
