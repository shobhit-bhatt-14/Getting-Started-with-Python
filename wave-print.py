def wavePrint(arr, n, m) :
    for i in range(m) :
        if i & 1 :
            for j in range(n-1,-1,-1) :
                print(arr[j][i], end=' ')
        else :
            for j in range(n) :
                print(arr[j][i], end=' ')

s = input().split()
n , m = int(s[0]) , int(s[1])
arr = [[j for j in input().split()] for i in range(n)]
wavePrint(arr, n, m)