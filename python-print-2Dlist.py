li = [[1,2,3,4], [5,6], [7,8,9], [0]]

# Method 1 native traversal
for i in li:
    for j in i:
        print(j, end=' ')
    print()

# Method 2 using join()
for i in li :
    print(' '.join([str(j) for j in i]))