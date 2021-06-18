# n -> no. of rows/list | m -> no. of columns/elements in each individual list
s = input().split()
n, m = int(s[0]), int(s[1])
# if no m is specified then it is a jagged list

# input for each list given in single line
p = input().split()
li = [[int(p[m*i+j]) for j in range(m)] for i in range(n)]

print(li)