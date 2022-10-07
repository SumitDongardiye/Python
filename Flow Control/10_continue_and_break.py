shopping_items=["Eggs","Bananas","Maggi","Bread","Curd","Stale Apple"]

for item in shopping_items:
    if item!="Stale Apple":
        print(f"{item} added to cart")

print()
print()

for item in shopping_items:
    if item=="Stale Apple":
        continue
    print(f"{item} added to cart")

print()
print()

for item in shopping_items:
    if item=="Bread":
        break
    print(f"{item} added to cart")