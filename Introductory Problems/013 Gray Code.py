n = int(input())
base = [""]

for ele in range(n) :
    base1 = ["0" + ele for ele in base]
    base2 = ["1" + ele for ele in base]
    base2.reverse()
    base = base1 + base2
for ele in base :
    print(ele)