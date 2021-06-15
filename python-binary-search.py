def binarySearch(arr, n, x) :
    start = 0
    end = n-1
    mid = 0
    while start<=end:
        mid = (start+end)//2
        
        if x<arr[mid]:
            end = mid-1
            
        elif x>arr[mid]:
            start = mid+1
            
        else:
            return mid
        
    return 0

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
res = binarySearch(arr, n, x)
if res:
    print('{} found at index {}'.format(x,res))
else:
    print('Invalid Search')