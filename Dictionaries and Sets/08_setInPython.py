countries={"India","Usa","UK","Spain","Germany"}

for item in countries:
    print(item)

print()
print("Usa" in countries)

print()

countries.add("Italy")
for item in countries:
    print(item)

countries.update(["Srilanka","Cuba","Bali"])
print()
for item in countries:
    print(item)

print()
print(len(countries))

print()

countries.remove("Cuba")
for item in countries:
    print(item)

print()

countries.discard("Pakistan")  #Pakistan is not present still discard function will not give any error
# countries.clear() -> it is used to clear all the elements in the  set

# del countries ->it deletes the set with name
