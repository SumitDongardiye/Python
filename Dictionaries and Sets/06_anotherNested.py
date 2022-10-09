child1={
        "name":"Kajol",
        "year":1992,
    }

child2={
        "name":"Shourya",
        "year":1998,
    }

child3={
        "name":"Aayushi",
        "year":1998,
    }

myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3,
}

print(myfamily)
print()

for items in myfamily:
    print(items)
print()

for items in myfamily:
    print(myfamily[items])
print()

for items in myfamily.values():
    print(items)
print()

for x in myfamily.items():
    print(x)
print()

for x,y in myfamily.items():
    print(x,y)

print()

for nesteditems in myfamily.values():
    for x in nesteditems.values():
        print(x)
print()

for x in myfamily.values():
    for y,z in x.items():
        print(y,z)