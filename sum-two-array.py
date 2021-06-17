def sumArrays(arr1, n, arr2, m) :
    res = []
    carry = 0
    i = n-1
    j = m-1
    for x in range(max(n,m)):
        if i>=0 and j>=0:
            sum = (arr1[i]+arr2[j]+carry)
            i -= 1
            j -= 1
        elif i<0:
            sum = arr2[j]+carry
            j -= 1
        elif j<0:
            sum = arr1[i]+carry
            i -= 1
        res.append(sum%10)
        carry = sum//10

    if len(res) == max(n,m):
        res.append(carry)

    res.reverse()
    return res

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

print(sumArrays(arr1, n, arr2, m))