class User:
    def __init__(self,name,user_id):
        self.__name=name
        self.__user_id=user_id

    def get_name(self):
        return self.__name
    
    def get_userid(self):
        return self.__user_id
    
    def set_name(self,name):
        self.__name=name
    
    def set_userid(self,user_id):
        self.__user_id=user_id

user1=User("name",1)

user1.set_name("Sumit")
user1.set_userid(33)

print(user1.get_name())
print(user1.get_userid())