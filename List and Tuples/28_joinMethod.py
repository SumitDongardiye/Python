#Join only works with strings

fruits=[
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Litchi",
    "Watermelon",
]

for fruit in fruits:
    print(fruit)
separator=","

value=separator.join(fruits)
print(value)