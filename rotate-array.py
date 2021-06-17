def rotateA(arr, n, d) :
    temp = arr[:d]
    del arr[:d]
    arr.extend(temp)

n = int(input())
arr = list(map(int, input().split()))
d = int(input())
rotateA(arr, n, d)
print(arr)