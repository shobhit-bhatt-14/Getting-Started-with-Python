n = int(input())
e = (2*n)+1
i = 0
while i<n :
    j = 1
    while j<=e :
        if j==i+1 or j==n+1 or j==e-i :
            print('*',end='')
        else :
            print('0',end='')
        j = j+1
    print()
    i = i+1