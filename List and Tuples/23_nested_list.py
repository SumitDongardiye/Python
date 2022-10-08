grocery_bag=[
    ["bread","butter"],
    ["bread","butter","unavailable","cream"],
    ["bread","butter","cream","unavailable","corn"],
    ["bread","butter","cream","corn","apple","unavailable"],
    ["bread","butter","cream","corn","apple","unavailable","teabag","unavailable"],
]

for item in grocery_bag:
    if "unavailable" not in item:
        print(item)

        for i in item:
            print(i)
    else:
        print(item.count("unavailable"))