def selectionSort(arr, n):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

n = int(input())
arr = list(map(int, input().split()))
selectionSort(arr, n)
print(arr)