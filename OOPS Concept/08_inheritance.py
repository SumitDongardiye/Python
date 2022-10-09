class Person:
    def __init__(self,name):
        self.name=name
    
    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name,roll_no):
        # super().__init__(name)
        self.roll_no=roll_no
        Person.__init__(self,name)
    def get_roll_no(self):
        return self.roll_no
    
p1=Person("Sumit")
print(p1.get_name())

p2=Student("Sum",1)
print(p2.get_name())
print(p2.get_roll_no())