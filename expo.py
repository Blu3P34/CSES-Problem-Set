def Exponenential_function(a, b):
    c = 1
    for i in range(b):
        c = c * a
    return c
print(Exponenential_function(3,9))