#Calculate Sum and Average 
def find_avg_marks(marks):
    SOM = sum(marks)
    no_of_subject = len(marks)
    avg_marks= SOM/no_of_subject
    return SOM , avg_marks      #positional argument

#Calculate grade 
def cal_grade(avg_marks):
    if avg_marks >=80:
        grade = 'A'
    elif avg_marks >=65:
        grade = 'B'
    elif avg_marks >=50:
        grade = 'C'
    else :
        grade ='F'
    return grade 

#Studedents marks 

marks =[45,50,50,81,55,85]
SOM, avg_marks = find_avg_marks(marks)

print(f"Total no is {SOM}  : And Average marks is {avg_marks}  ")      #It prints the total no and avg marks 


# Calculate Grade 

grade = cal_grade(avg_marks)
print("Students Grade : ",grade)