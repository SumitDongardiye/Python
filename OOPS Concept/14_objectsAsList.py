counter=0

class Student:
    def __inti__(self):
        self.__roll_no=0
        self.__name="Unknown"
    
    def set_values(self,name,roll_no):
        self.__name=name
        self.__roll_no=roll_no
    
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    
    def get_values(self):
        return self.__name,self.__roll_no

student_obj_list=[Student() for i in range(2)]

def fetch_values():
    global counter
    counter+=1
    temp_name=input("Enter the Name: ")
    return temp_name,counter


for item in range(0,len(student_obj_list)):
    x,y=fetch_values()
    student_obj_list[item].set_values(x,y)

for item in range(0,len(student_obj_list)):
    print("Name: ",student_obj_list[item].get_name())
    print("Roll No: ",student_obj_list[item].get_roll_no())
    print("Tuple: ",student_obj_list[item].get_values())