def swap(a,b):
    a,b=b,a
    return a,b

x,y=10,20
print(f"Before Swap x={x},y={y}")
x,y=swap(x,y)
print(f"After Swap x={x},y={y}")
