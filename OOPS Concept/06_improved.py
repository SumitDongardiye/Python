class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    
    def print_values(self):
        print(self.roll_no)
        print(self.name)
    
s1=Student(1,"A")
s2=Student(2,"B")

temp_name=input("Enter your Name: ")
temp_roll_no=int(input("Enter your Roll No: "))

s3=Student(temp_roll_no,temp_name)

s1.print_values()
s2.print_values()
s3.print_values()