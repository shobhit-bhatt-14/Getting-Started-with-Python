def f_2_c(x):
    cel = (x-32)*5
    cel = cel/9
    return int(cel)

def printTable(start,end,step):
    for i in range(start, end+1, step):
        print(i,end='\t')
        print(f_2_c(i))

s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)