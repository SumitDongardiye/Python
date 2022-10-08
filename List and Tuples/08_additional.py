choice="_"
grocery_items=[]

while choice!="EXIT":
    choice=input("Enter name of item: ")
    if choice!="EXIT":
        grocery_items.append(choice)

print(grocery_items)