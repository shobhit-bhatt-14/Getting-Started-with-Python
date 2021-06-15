def selectionSort(arr, n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

n = int(input())
arr = list(map(int, input().split()))
selectionSort(arr, n)
print(arr)