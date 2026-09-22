import pandas as pd

df = pd.read_csv('students_marks.csv')
# print(df)

name = input("Enter the students name ")
print(df[df['Student Name']==name])

add_details= pd.DataFrame([{
    "Roll No" : 97,
    'Student Name' : 'Maniraj Tiwari',
    'Hindi':55,
    'English':66,
    'Maths':85,
    'Physics':45,
    'Chemistry':67
}])
df = pd.concat([df, add_details], ignore_index=True)
print(df)

df=df.drop(columns=['Roll No'])
print(df)

df["Roll No."] = range(1, len(df) + 1)
df["Roll No."] = df["Roll No."].astype(int)