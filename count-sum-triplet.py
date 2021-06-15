def findTriplet(arr, n, x) :
    count = 0
    for i in range(n-2):
        if arr[i]>x:
            continue
        for j in range(i+1,n-1):
            a = arr[i]+arr[j]
            if a>x:
                continue
            for k in range(j+1,n):
                b = a+arr[k]
                if b==x:
                    count = count+1
    return count

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(findTriplet(arr, n, x))