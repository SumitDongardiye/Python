set1={"a","b","c","d","e"}
set2={1,2,3,4,"a","b","c"}

set3=set1.intersection(set2)
print(set3)

set1.intersection_update(set2)
print(set1)