n = int(input())
e = 2*n
i = 1
while i<=n :
    j = 1
    while j<=e :
        if j<=i :
            print(j,end='')
        elif j>e-i :
            print(e+1-j,end='')
        else :
            print(' ',end='')
        j = j+1
    print()
    i = i+1