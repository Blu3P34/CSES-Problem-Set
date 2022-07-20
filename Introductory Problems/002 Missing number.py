n = int(input())
b = 0
list = map(int, input().split())
for i in list :
    b = b + i
print(n*(n + 1)//2-b)




