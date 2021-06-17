def pushZerosAtEnd(arr, n) :
    temp = 0
    for i in range(n):
        if arr[i] != 0:
            arr[temp],arr[i] = arr[i],arr[temp]
            temp += 1

n = int(input())
arr = list(map(int, input().split()))
pushZerosAtEnd(arr, n)
print(arr)