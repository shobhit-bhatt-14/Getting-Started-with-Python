def sortZeroesAndOne(arr, n) :
    ch = 0
    for i in range(n):
        if arr[i]==0:
            temp = arr[ch]
            arr[ch] = arr[i]
            arr[i] = temp
            ch = ch+1

n = int(input())
arr = list(map(int, input().split()))
sortZeroesAndOne(arr, n)
print(arr)