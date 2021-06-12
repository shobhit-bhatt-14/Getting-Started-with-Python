n = int(input())
ch = True
for i in range(n,0,-1) :
    j = 0
    while j<i :
        print(int(ch), end='')
        j = j+1
    print()
    ch = int(not ch)