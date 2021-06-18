# List with uneven length of list (or Jagged List )
li = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]]

# Accessing and printing each individual List inside List
print("Each individual List")
for i in li :
    print(i, end="\t")
print()

# Accessing and printing each individual element inside Jagged List
print("Each element inside the List")
for i in range(len(li)) :
    for j in range(len(li[i])) :
        print(li[i][j], end='\t')
    print()