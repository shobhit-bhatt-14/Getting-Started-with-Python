# whole input given in single line
str = input().split()
n, m = int(str[0]), int(str[1])
s = str[2:]
li = [[int(s[m*i+j]) for j in range(m)] for i in range(n)]

print(li)