n = int(input())
for i in range(1,n+1) :
    sp = i-1
    while sp>0 :
        print(' ',end='')
        sp = sp-1
    j = i
    while j<=n :
        print(j,end='')
        j = j+1
    print()
for i in range(n-1,0,-1) :
    sp = i-1
    while sp>0 :
        print(' ',end='')
        sp = sp-1
    j = i
    while j<=n :
        print(j,end='')
        j = j+1
    print()