def mergeA(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i<len(arr1) or j<len(arr2):
        res.extend(arr1[i:len(arr1)])
        res.extend(arr2[j:len(arr2)])

    return res

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(mergeA(arr1,arr2))