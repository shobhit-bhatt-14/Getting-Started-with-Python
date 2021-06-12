n = int(input())
i = 1
while i <= n :
    sp = n-i
    j = 1
    a = i
    while sp > 0 :
        print(" ", end='')
        sp = sp-1
    while j < 2*i :
        print(a, end='')
        if j>=i :
            a = a-1
        else :
        	a = a+1
        j = j+1
    print()
    i = i+1