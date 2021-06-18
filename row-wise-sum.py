def rowSum(arr, n, m) :
    for x in arr :
        temp = 0
        for y in x :
            temp += int(y)
        print(temp, end=' ')

s = input().split()
n , m = int(s[0]) , int(s[1])
arr = [[j for j in input().split()] for i in range(n)]
rowSum(arr, n, m)