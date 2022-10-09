# Python Program for factorial of a number
# ans=1
# def factorial(n):
#     for i in range(1,n+1):
#         global ans
#         ans=ans*i

# a=int(input("Enter the Number: "))
# factorial(a)
# print(f"The factorial of {a} is: ",ans)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

a=int(input("Enter the Number: "))

print(f"The factorial of {a} is: ",factorial(a))