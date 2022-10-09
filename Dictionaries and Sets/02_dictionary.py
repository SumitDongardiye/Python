users={
    123:"@sumit",
    124:"@atulya",
    125:"@manish",
}

users[123]="@sumitd"
print(users[123])
print(len(users))

for item in users:
    print(item)
print()

for item in users:
    print(users[item])
print()
for item in users.values():
    print(item)
print()

for x,y in users.items():
    print(x,y)
print()

if 125 in users:
    print("Key exists")

#Add items in Dictionary

users[126]="@avi"
users[127]="@aditi"
users[128]="@adivik"
print()

for x,y in users.items():
    print(x,y)
print()

#Remove Item
users.pop(126)

for x,y in users.items():
    print(x,y)
print()

users.popitem()

for x,y in users.items():
    print(x,y)
print()

#Delete Item
del users[124]

for x,y in users.items():
    print(x,y)
print()