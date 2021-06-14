def swapAlternate(arr, n) :
    for i in range(0, n-1, 2):
        arr[i],arr[i+1] = arr[i+1],arr[i]

n = int(input())
arr = list(map(int, input().split()))
swapAlternate(arr, n)
print(arr)