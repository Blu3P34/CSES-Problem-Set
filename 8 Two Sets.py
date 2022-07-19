n = int(input())
if n*(n + 1)//2 %2 == 0 :
    print("YES")
    if n %2 == 0 :
        print(n//2)
        for ele in range(1, n//4 + 1) :
            print(ele, n + 1 - ele, sep = " ", end = " " )
        print("\n" + str(n//2))
        for ele in range(n//4 + 1, n//2 + 1) :
            print(ele, n + 1 - ele, sep = " ", end = " " )
    else :
        print((n - 1)//2)
        for ele in range(1, (n + 1)//4) :
            print(ele, n + 1 - ele, sep = " ", end = " " )
        print(3*(n + 1)//4)
        print((n + 1)//2)
        for ele in range((n + 1)//4 + 1, (n + 1)//2) :
            print(ele, n + 1 - ele, sep = " ", end = " " )
        print((n + 1)//4, (n + 1)//2, sep = " ")
else :
    print("NO")