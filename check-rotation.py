def checkRotation(arr, n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return i+1
    return 0

n = int(input())
arr = list(map(int, input().split()))
print(checkRotation(arr, n))