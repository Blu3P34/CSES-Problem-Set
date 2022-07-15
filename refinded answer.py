#1 weird algorithm
#2 missing number 
#3 repition

x=m=0
c=''
 
for i in input():
    x, c = x*(c==i)+1, i
    m = m if m > x else  x
    
print("3 " + m)
 
#4 increasing array