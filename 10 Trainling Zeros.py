#The math is roght, put Python takes to much damn time to compile

n = int(input())
f = 1
i = 0
for ele in range(2, n + 1) :
    while ele %5 == 0 :
        ele = ele//5
        i = i + 1
print(i)

