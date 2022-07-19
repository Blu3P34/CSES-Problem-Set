n = int(input())
k = 2
m = n - 1 if n%2 == 0 else n
if n in [2, 3] :
    print("NO SOLUTION")
else :
    if n == 1 :
        print(n)
    else :
        while k != m :
            print(k, end = " ")
            k = k + 2 if k + 2 <= n else 1
        print(m)