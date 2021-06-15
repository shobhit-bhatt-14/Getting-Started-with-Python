def findUnique(arr, n) :
    li = []
    for i in arr:
        if i not in li:
            li.append(i)
        else:
            li.remove(i)
    return li

n = int(input())
arr = list(map(int, input().split()))
print(findUnique(arr, n))