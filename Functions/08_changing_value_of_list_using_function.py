def myfunction(val):
    print(val[0])
    val[0]=0
    print(val[0])

list=[10,20,30,40,50,60]
myfunction(list)
print()
print(list)