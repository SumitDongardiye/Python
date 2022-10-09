counter=0
class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    def print_values(self):
        print(self.roll_no)
        print(self.name)


def fetch_values():
    global counter
    counter+=1
    temp_name=input("Enter you Name: ")
    return counter,temp_name


x,y=fetch_values()
s1=Student(x,y)
s1.print_values()

x,y=fetch_values()
s2=Student(x,y)
s2.print_values()
