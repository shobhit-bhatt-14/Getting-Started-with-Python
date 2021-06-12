n = int(input())
i = 1 
mid = (n+1)//2
while i<=n :
    if i>mid :
        sp = i-mid
        j = (2*(n-i))+1
        while sp>0 :
            print(' ',end='')
            sp = sp-1
        while j>0 :
            print('*',end='')
            j = j-1
    else :
        sp = mid-i
        j = (2*i)-1
        while sp>0 :
            print(' ',end='')
            sp = sp-1
        while j>0 :
            print('*',end='')
            j = j-1
    print()
    i = i+1