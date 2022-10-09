maxsize=5

def create_stack():
    created_stack=[]
    return created_stack

def isfull(stack):
    if len(stack)==maxsize:
        print("Overflow")
    
    return len(stack)==maxsize

def push(stack,val):
    if isfull(stack):
        return
    
    stack.append(val)
    print(f"The value {val} has been pushed.")

def peek(stack):
    if len(stack)==0:
        print("Underflow")
        return
    print(stack[-1])

def is_empty(stack):
    if len(stack)==0:
        print("Underflow")
    return len(stack)==0

def pop(stack):
    if is_empty(stack):
        return
    temp=stack.pop()
    print(f"{temp} has been popped from the stack.")

stack=create_stack()

peek(stack)
pop(stack)
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
push(stack,50)
push(stack,60)
pop(stack)
peek(stack)