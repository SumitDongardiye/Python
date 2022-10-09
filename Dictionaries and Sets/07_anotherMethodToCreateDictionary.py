x=('Key1','Key2','Key3')
y=(0,1,2)

newDictionary=dict.fromkeys(x,y)

print(newDictionary)

a=newDictionary.get('Key1')
print(a)

b=newDictionary.keys()
print(b)