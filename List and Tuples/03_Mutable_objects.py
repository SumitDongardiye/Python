grocery=["Eggs","Milk","Bread","Butter","iPhone"]
another_grocery=grocery

print(id(grocery))
print(id(another_grocery))

grocery+=["tea"]

print(id(grocery))
print(id(another_grocery))