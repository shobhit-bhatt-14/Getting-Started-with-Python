def pairSum(arr, n, x) :
    count = 0
    for i in range(n-1):
        if arr[i]>x:
            continue
        for j in range(i+1,n):
            if arr[j]>x:
                continue
            elif arr[i]+arr[j] == x:
                count = count+1
    return count

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(pairSum(arr, n, x))