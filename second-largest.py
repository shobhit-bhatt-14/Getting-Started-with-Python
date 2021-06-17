def secondLargest(arr) :
    arr = list(set(arr))
    arr.sort()
    if len(arr)<=1 :
        return 'Not Possible !!'
    else :
        return arr[-2]

arr = list(map(int, input().split()))
print(secondLargest(arr))