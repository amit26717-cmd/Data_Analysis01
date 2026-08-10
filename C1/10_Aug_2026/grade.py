mark = int(input("Enter your marks :- "))
# if mark >= 90:
#     print(f"you got Grade A+ with the number of {mark}")
# elif mark >= 80:
#     print(f"You got Grade A with the number of {mark}")
# elif mark >=70 :
#     print(f"You got the Grade B with the number of {mark}")
# else :
#     print(f"Unfortunatly you fail with the number of {mark}")

if mark >=90:
    Grade = "A+"
elif mark >= 80:
    Grade = "A"
elif mark >=70:
    Grade = "B"
elif mark >=60:
    Grade = "C"
elif mark >=50:
    Grade = "D"
else :
    Grade = "Fail"
print(f"You got thr Grade {Grade} with the number of {mark}")