class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    
s1=Student(1,"A")
s2=Student(2,"B")

print(s1.roll_no)
print(s1.name)
print(s2.roll_no)
print(s2.name)

temp_name=input("Enter your Name: ")
temp_roll_no=int(input("Enter your Roll No: "))

s3=Student(temp_roll_no,temp_name)
print(s3.roll_no)
print(s3.name)
