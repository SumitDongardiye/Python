import enum


a=b=c=d=e=10
print(e)

x,y,z=1,2,5
print(x)
print(y)
print(z)

print("Let's talk about unpacking a tuple")

values=(1,2,10)
print(values)
q,w,e=values
print(q)
print(w)
print(e)

print()

list=[1.0,4.2,5.9]
a,b,c=list
print(a)
print(b)
print(c)

print()

for index,char in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(index,char)

print()

for values in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(values)

print()

for values in enumerate("abcdefghijklmnopqrstuvwxyz"):
    index,char=values
    print(index,char)

print()

user_infor="Sumit",100,"India",1800

name,age,country,year=user_infor
print(name)
print(age)
print(country)
print(year)

print()

land=("Delhi",12,100.0,150.5)
print(land[1]*land[2]*land[3])