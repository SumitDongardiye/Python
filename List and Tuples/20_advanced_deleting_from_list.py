numbers=[3,7,200,201,203,214,281,300,301,302,309,40001,40009]

min_allowed=200
max_allowed=400
stop=0
start=0

for index,value in enumerate(numbers):
    if value>=min_allowed:
        stop=index
        break
del numbers[:stop]

for index in range(len(numbers)-1,-1,-1):
    if(numbers[index]<=max_allowed):
        start=index+1
        break

del numbers[start:]
print(numbers)