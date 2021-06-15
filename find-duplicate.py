def findDuplicate(arr, n) :
    li = []
    res = []
    for i in arr:
        if i not in li:
            li.append(i)
        elif i not in res:
            res.append(i)
    return res

n = int(input())
arr = list(map(int, input().split()))
print(findDuplicate(arr, n))