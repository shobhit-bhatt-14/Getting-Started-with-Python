n = int(input())
mid = (n+1)//2
for i in range(1,mid+1) :
    sp = mid-i
    while sp>0 :
        print(' ',end='')
        sp = sp-1
    j = (2*i)-1
    while j>0 :
        print('*',end='')
        j = j-1
    print()
for i in range(mid-1,0,-1) :
    sp = mid-i
    while sp>0 :
        print(' ',end='')
        sp = sp-1
    j = (2*i)-1
    while j>0 :
        print('*',end='')
        j = j-1
    print()