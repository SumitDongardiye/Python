class Citizen:
    def __init__(self,aadhar_id):
        self.aadhar_id=aadhar_id
    
    def get_aadhar(self):
        return self.aadhar_id
    
class Person:
    def __init__(self,name):
        self.name=name
    
    def get_name(self):
        return self.name

class Student(Person,Citizen):
    def __init__(self, name,roll_no,aadhar_id):
        # super().__init__(name)
        self.roll_no=roll_no
        Person.__init__(self,name)
        Citizen.__init__(self,aadhar_id)
    def get_roll_no(self):
        return self.roll_no


p2=Student("Sum",1,694564319466)
print(p2.get_name())
print(p2.get_roll_no())
print(p2.get_aadhar())


        