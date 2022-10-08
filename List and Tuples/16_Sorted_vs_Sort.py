list1=["Mike","Chris","eric","Andy","Chloe","Joe","Po","Z"]

# list2=sorted(list1,key=str.casefold)
# print(list2)

# list1.sort(key=str.casefold)
# print(list1)

new_string=sorted("The driven jocks help fax my big quiz",key=str.casefold)
print(new_string)

list1.sort(reverse=True)
print(list1)

list2=sorted(list1,key=str.casefold,reverse=True)
print(list2)