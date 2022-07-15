a = input()
k = m = 1
for ele in range(1,len(a)) :
    if a[ele] == a[ele - 1] :
        k = k + 1
        m = k if k > m else m 
    else : 
        k = 1
print(m)

