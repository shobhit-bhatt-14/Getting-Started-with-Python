n = int(input())
l = (2*n)-1
for i in range(0,n) :
    p = n
    for a in range(0,i) :
        print(p,end='')
        p = p-1
    for b in range(0,l) :
        print(p,end='')
    l = l-2
    p = p+1
    for c in range(0,i) :
        print(p,end='')
        p=p+1
    print()
l = l+4
for i in range(n-2,-1,-1) :
    p = n
    for a in range(0,i) :
        print(p,end='')
        p = p-1
    for b in range(0,l) :
        print(p,end='')
    l = l+2
    p = p+1
    for c in range(0,i) :
        print(p,end='')
        p=p+1
    print()