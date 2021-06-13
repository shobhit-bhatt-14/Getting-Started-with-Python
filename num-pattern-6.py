n = int(input())
l = 2*n
m = (n+1)//2
p = n*n

for i in range(1,p,l) :
    for j in range(i,i+n) :
        print(j,end=' ')
    print()

if n & 1 :
    q = p-l+1
else :
    q = j+1

for i in range(q,0,-l) :
    for j in range(i,i+n) :
        print(j,end=' ')
    print()