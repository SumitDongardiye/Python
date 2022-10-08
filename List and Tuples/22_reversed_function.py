numbers=[301,392,7,11,201,40001,320,1,31,364]

min_allowed=200
max_allowed=400

top_index=len(numbers)-1

for index,value in enumerate(reversed(numbers)):
    if value<min_allowed or value>max_allowed:
        del numbers[top_index-index]

print(numbers)