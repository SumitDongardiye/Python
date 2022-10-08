choice="_"
grocery_items=[]

while choice!='0':
    if choice in "1234":
        print("Adding {0} to cart.".format(choice))

        if choice=="1":
            grocery_items.append("Apple")
        if choice=="2":
            grocery_items.append("Milk")
        if choice=="3":
            grocery_items.append("Mango")
        if choice=="4":
            grocery_items.append("Orange")
    else:
        print("Add items from available ones: ")
        print("1.Apple")
        print("2.Milk")
        print("3.Mango")
        print("4.Orange")

    choice=input()
print(grocery_items)