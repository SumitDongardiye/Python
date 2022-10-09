class Person:
    def __init__(self,name):
        self._name=name

class Student(Person):
    def __init__(self, name,id):
        self.__id=id
        Person.__init__(self,name)

    def printval(self):
        return self._name,self.__id

s1=Student("Sumit",1)
print(s1.printval())