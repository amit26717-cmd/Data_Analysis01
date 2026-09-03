# write a program create a calculator that perform addition subtraction multiplicati and division using function 
# input number into try block
# use except block to handle invailid input ,unsuported operation , zero division 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
        if b!=0:
            return a/b
        else :
            print("Can't divide by Zero ")
        

while True:
     try :
        num1 = float(input("Enter the first number  : "))
        num2 = float(input("enter the second number : "))
        operation = input("Enter the operation to perform : ")

        if operation == '+' :
            result = add(num1,num2)
        elif operation =='-':
            result = sub(num1,num2)    
        elif operation == '*':
            result = multi(num1,num2)
        elif operation == '/':
            result = divi(num1,num2)
        else :
            raise ValueError ("invailid input ")
     
        print(result)
        break 
     except ValueError as e:
        print("Error:", e)
        print("try again.\n")

     except ZeroDivisionError as e:
        print("Error:", e)
        print("try again.\n")



