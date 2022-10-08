instock_items=["Apple","Mango","Bread","Milk"]

choice="_"
grocery_items=[]

while choice!='0':
    if choice in "1234":
        print("Adding {0} to cart.".format(choice))

        if choice=="1":
            grocery_items.append("Apple")
        if choice=="2":
            grocery_items.append("Mango")
        if choice=="3":
            grocery_items.append("Bread")
        if choice=="4":
            grocery_items.append("Milk")
    else:
        print("0 to Exit if not then, ")
        print("Add items to basket")
        for number,item in enumerate(instock_items):
            print(f"{number+1}.{item}")

    choice=input()

print(grocery_items)