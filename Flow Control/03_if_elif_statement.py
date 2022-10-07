name=input("Enter your Name: ")
age=int(input("Enter your age: "))

if age<18:
    print(f"{name} Can't Vote.")
elif age>1000:
    print(f"{name} this is not Possible.")
elif age==18:
    print(f"{name} you can Vote.")
else:
    print(f"{name} you can Vote.")