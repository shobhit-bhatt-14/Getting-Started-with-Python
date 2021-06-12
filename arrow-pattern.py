n = int(input())
mid = (n+1)//2
i = 1
while i<=n :
    if i<=mid :
        sp = i
        while sp>1 :
            print(' ',end='')
            sp = sp-1
        j = i
        while j>0 :
            print('* ',end='')
            j = j-1
            
    else :
        sp = n-i
        while sp>0 :
            print(' ',end='')
            sp = sp-1
        j = n+1-i
        while j>0 :
            print('* ',end='')
            j = j-1
        
    print()
    i = i+1