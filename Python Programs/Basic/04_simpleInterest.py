# Python Program for simple interest
def simpleInterest(p,r,t):
    return (p*r*t)/100

p=int(input("Enter Principal: "))
r=int(input("Enter Rate: "))
t=int(input("Enter Time: "))

ans=simpleInterest(p,r,t)

print("The simple interset is: ",ans)