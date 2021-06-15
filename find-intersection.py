def findIntersection(arr1, n, arr2, m) :
    res = []
    for i in arr1:
        if i in arr2:
            res.append(i)
            arr2.remove(i)
    return res

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
print(findIntersection(arr1, n, arr2, m))