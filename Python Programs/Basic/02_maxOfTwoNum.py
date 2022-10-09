# Maximum of two numbers in Python

def Max(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))

print(f"The greater Numbers between {a} and {b} is: ",Max(a,b))