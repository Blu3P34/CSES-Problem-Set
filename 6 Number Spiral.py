from re import X


t = int(input())
for ele in range(t) :
    lst = list(map(int, input().split()))
    x = lst[0] 
    y = lst[1]
    if x >= y :
        z = x*x - y + 1 if x*x %2 == 0 else x*x - 2*x + y + 1
    else :
        z = y*y - 2*y + x + 1 if y*y %2 == 0 else y*y - x + 1
    print(z)
