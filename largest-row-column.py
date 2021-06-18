def largestRowCol(arr, n, m) :
    sumC, sumR, tempC, tempR, indexC, indexR = -1, -1, 0, 0, -1, -1
    for i in range(n) :
        for j in range(m) :
            tempR += int(arr[i][j])
        if tempR>sumR :
            sumR = tempR
            indexR = i
        tempR = 0
    for i in range(m) :
        for j in range(n) :
            tempC += int(arr[j][i])
        if tempC>sumC :
            sumC = tempC
            indexC = i
        tempC = 0

    if indexC == indexR == -1 :
        print("Does not exist")
    elif sumC > sumR :
        print("column {} {}".format(indexC,sumC))
    elif sumR >= sumC :
        print("row {} {}".format(indexR,sumR))

s = input().split()
n , m = int(s[0]) , int(s[1])
arr = [[j for j in input().split()] for i in range(n)]
largestRowCol(arr, n, m)