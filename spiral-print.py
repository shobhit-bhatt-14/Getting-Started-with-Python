def spiralPrint(arr, n, m) :
    top, bottom, left, right = 0, n-1, 0, m-1
    d = 0

    while top<=bottom and left<=right :
        if d == 0 :
            for x in range(left,right+1) :
                print(arr[top][x], end=' ')
            top += 1
        elif d == 1 :
            for x in range(top,bottom+1) :
                print(arr[x][right], end=' ')
            right -= 1
        elif d == 2 :
            for x in range(right,left-1,-1) :
                print(arr[bottom][x], end=' ')
            bottom -= 1
        elif d == 3 :
            for x in range(bottom,top-1,-1) :
                print(arr[x][left], end=' ')
            left += 1
        
        d = (d+1)%4

s = input().split()
n , m = int(s[0]) , int(s[1])
arr = [[j for j in input().split()] for i in range(n)]
spiralPrint(arr, n, m)