def Exponenential_function(base , exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result
print(Exponenential_function(3,5))