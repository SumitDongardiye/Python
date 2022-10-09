users={
    123:"@sumit",
    124:"@atulya",
    125:"@manish",
}

users1=users.copy()

for x,y in users1.items():
    print(x,y)
print()
users2=dict(users)

for x,y in users2.items():
    print(x,y)