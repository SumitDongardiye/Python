shopping_items=["Eggs","Bananas","Maggi","Bread","Curd","Stale Apple"]

item_find="Stale Apple"
found=None

for i in range(len(shopping_items)):
    if(shopping_items[i]==item_find):
        found=i
        break

print(found)