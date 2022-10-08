numbers=[301,392,7,11,201,40001,320,1,31,364]

min_allowed=200
max_allowed=400

for index in range(len(numbers)-1,-1,-1):
    if(numbers[index]<min_allowed or numbers[index]>max_allowed):
        del numbers[index]

print(numbers)