#The math is right, put Python takes to much damn time to compile

n = int(input())
f = 5
i = 0
while n >= f :
    i += n//f
    f *= 5
print(i)

