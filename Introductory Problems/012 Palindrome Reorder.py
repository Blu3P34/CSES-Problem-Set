from collections import defaultdict

n = input()

dict = defaultdict(int)
for ele in range(len(n)) :
    dict[n[ele]] += 1

odd_num = 0
odd_char = ""

for key in dict :
    if dict[key] %2 == 1 :
        odd_num = odd_num + 1 
        odd_char = key

if odd_num > 1 or odd_num == 1 and len(n)%2 == 0 :
    print("NO SOLUTION")

else :
    first_half = ""
    second_half = ""
    for key in sorted(dict.keys()) :
        w = dict[key]//2*key if dict[key] %2 == 0 else ""
        first_half = first_half + w
        second_half = w + second_half 

    print(first_half + odd_char*dict[odd_char] + second_half)
