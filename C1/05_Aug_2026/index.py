a = int(input("Enter the number : - "))
b = float(input("Enter the number : - "))
sum = a+ b
print(f"the sum of {a} and {b} is {sum}")

for i in range (1, 10+1) :
    print(f"3 x {i} = {3*i}")
arr = [[0,0] , [0,0]]
for i in range (2):
    for j in range (2):
        arr[1][j] = int(input(f"enter element {i+1} : "))

for row in  arr:
        print(arr)