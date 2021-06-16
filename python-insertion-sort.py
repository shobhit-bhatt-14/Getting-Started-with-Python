def insertionSort(arr, n):
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0:
            if temp<arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j = j-1
        arr[j+1] = temp

n = int(input())
arr = list(map(int, input().split()))
insertionSort(arr, n)
print(arr)