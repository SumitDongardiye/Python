grocery=["Eggs","Milk","Bread","Butter","iPhone"]
another_grocery=grocery.copy()

print(id(grocery))
print(id(another_grocery))

grocery+=["tea"]

print(id(grocery))
print(id(another_grocery))