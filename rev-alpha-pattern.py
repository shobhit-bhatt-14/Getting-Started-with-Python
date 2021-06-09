n = int(input())
a = 64
i = n
while i>0 :
    j = 0
    while j<=(n-i) :
        ch = chr(a+i+j)
        print(ch, end='')
        j = j+1
    print()
    i = i-1