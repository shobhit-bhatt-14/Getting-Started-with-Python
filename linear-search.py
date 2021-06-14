def linearSearch(n, li, s):
    ch = False
    for i in range(n):
        if li[i] == s:
            res = [s,i]
            return res     
    return ch

n = int(input())
li = list(map(int,input().split()))
s = int(input())
res = linearSearch(n,li,s)

if res:
    print('{} present at index {}'.format(res[0],res[1]))
else:
    print('{} not found'.format(s))