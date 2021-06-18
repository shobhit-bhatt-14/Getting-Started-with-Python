# 2D List or List of List
li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Accessing and printing each individual List inside List
print("Each individual List")
for i in li :
    print(i, end="\t")
print()

# Accessing and printing each individual element inside List of List (2D List)
print("Each element inside the List")
for i in range(len(li)) :
    for j in range(len(li[i])) :
        print(li[i][j], end='\t')
    print()