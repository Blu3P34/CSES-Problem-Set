x = y = 1
z = ""
for ele in input() :
    x = x + 1 if z == ele else 1
    y = x if x >= y else y
    z = ele
print(y)

