#  **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.

def myFunction(**kwargs):
    print("Youngest:{}".format(kwargs["child3"]))

myFunction(child1="A",child2="B",child3="C")