numbers=[3,7,200,201,203,214,281,300,301,302,309,40001,40009]

min_allowed=200
max_allowed=400
stop=0

for index,value in enumerate(numbers):
    if value>=min_allowed:
        stop=index
        break
    
del numbers[:stop]
print(numbers)

for index,value in enumerate(numbers):
    if value>=max_allowed:
        stop=index
        break
    
del numbers[stop:]
print(numbers)