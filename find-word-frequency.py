def countWordFreq(str) :
    dic = {}
    for w in str :
        dic[w] = dic.get(w,0)+1

    for x in dic :
        print(x, dic[x], sep=' : ', end=' | ')

str = input().split()
countWordFreq(str)