class Student:
    college="IIT"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no


s1=Student("A",1)
s2=Student("B",2)

print(s1.name)
print(s1.roll_no)
print(Student.college)

# Student.college="SVVV"

print(s2.name)
print(s2.roll_no)
print(Student.college)