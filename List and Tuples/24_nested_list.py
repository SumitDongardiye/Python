
grocery_bag=[
    ["bread","butter"],
    ["bread","butter","unavailable","cream"],
    ["bread","butter","cream","unavailable","corn"],
    ["bread","butter","cream","corn","apple","unavailable"],
    ["bread","butter","cream","corn","apple","unavailable","teabag","unavailable"],
]

for item in grocery_bag:
    for i in range(len(item)-1,-1,-1):
        if item[i]=="unavailable":
            del item[i]
    
    print(item)