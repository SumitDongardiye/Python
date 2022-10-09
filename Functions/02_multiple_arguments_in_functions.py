def my_function(*args):
    for arg in args:
        print("The {} child is: {}".format(args.index(arg),arg))

my_function("A","B","C")

