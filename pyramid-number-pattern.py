n = int(input())
e = (2*n)-1
i = 1
while i<=n :
    j = 1
    while j<=e :
        if j>n-i and j<n+1:
            print(n+1-j,end='')
        elif j>n and j<n+i :
            print(j-n+1,end='')
        elif j<n :
            print(' ',end='')
        j = j+1
    print()
    i = i+1