t = int(input())
for ele in range(t) :
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a >= b :
        t = a - b
        a = a - 2*t
        b = b - t
    else : 
        t = b - a 
        a = a - t
        b = b - 2*t
    if a >= 0 and a %3 == 0 :
        t1 = a//3*2
        print("YES")
    else :
        print("NO")
