name="Sumit" #Global Variable

def myfunction():
    global name
    print(name)
    name="Don" #Local Variable
    print(name)


myfunction()
