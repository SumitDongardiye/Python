from multiprocessing.synchronize import SemLock
from pickle import EMPTY_LIST


EMPTY_LIST=[]
print(EMPTY_LIST)

even=[2,4,6,8]
odd=[1,3,5,7]

num=even+odd

sorted_numbers=sorted(num)
print(sorted_numbers)

digits=list("123976102")
slice=num[4:]
print(slice)
new_list=num.copy()
print(new_list)