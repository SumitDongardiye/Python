name="Sumit"
print(name)

for i in name:
    print(i)

number="1,728,910:163;128'123,123"
value=""
sep=""

for char in number:
    if char.isnumeric():
        value+=char

print(value)

for char in number:
    if not char.isnumeric():
        sep+=char

print(sep)

print([int(val) for val in value])