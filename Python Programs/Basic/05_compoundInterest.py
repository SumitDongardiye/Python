# Python Program for compound interest

def compoundInterset(p,r,t):
    amount=p*(pow(1+r/100,t))
    ci=amount-p
    print("Compund Interset is: ",ci)

p=float(input("Enter Principal: "))
r=float(input("Enter Rate: "))
t=float(input("Enter Time: "))

compoundInterset(p,r,t)




