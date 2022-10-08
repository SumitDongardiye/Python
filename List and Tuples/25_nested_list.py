grocery_bag=[
    ["bread","butter"],
    ["bread","butter","unavailable","cream"],
    ["bread","butter","cream","unavailable","corn"],
    ["bread","butter","cream","corn","apple","unavailable"],
    ["bread","butter","cream","corn","apple","unavailable","teabag","unavailable"],
]

for item in grocery_bag:
    for i in item:
        if i != "unavailable":
            print(i)
    print()