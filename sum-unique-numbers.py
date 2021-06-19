def sumUnique(ls) :
    s = set()
    for i in ls :
        s.add(i)

    sum = 0
    for j in s :
        sum += j
    
    return sum

ls = list(map(int, input().split()))
print(sumUnique(ls))