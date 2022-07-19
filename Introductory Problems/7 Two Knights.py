k = int(input())
for n in range(1, k + 1) :
    c = n*n*(n*n-1)//2 if n > 1 else 0
    if n >= 3 :
        x = (n-1)*(n-2)*4
    else : 
        x = 0
    print(c - x)