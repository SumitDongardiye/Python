'''
__ is used for private variables
_ is used for protected variables
'''

class Student:
    def __init__(self,name,id):
        self.__name=name  #Private Variables
        self.__id=id

    def print_val(self):
        return self.__name,self.__id

s1=Student("Sumit",33)

print(s1.print_val())