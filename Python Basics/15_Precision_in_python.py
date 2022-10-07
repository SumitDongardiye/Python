print("{0}".format(22/7)) # default precision is 15

print("{0:<100}".format(22/7))
print("{0:<0100}".format(22/7)) #Empty space is filled with 0
print("{0:<100f}".format(22/7))  #6 characters after decimal

print("{0:<100f}".format(22/1))

print("{0:.2f}".format(22/7))
print("{0:.8f}".format(22/7))
print("{0:100.2f}".format(22/7))  # here 100 is filled with and .2f is precision
print("{0:3.6f}".format(22/7))


# Maximum Precision Available in Python=51




