n = int(input())
a = 64
i = 1
while i<=n :
    j = 0
    while j<i :
        ch = chr(a+i+j)
        print(ch, end='')
        j = j+1
    print()
    i = i+1