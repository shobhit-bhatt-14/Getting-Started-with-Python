def revList(li):
    for i in range(len(li)//2):
        li[i],li[-i-1] = li[-i-1],li[i]

# Method 1 using traversal and swapping
li = [1,2,3,4,5,6,7,8,9]
revList(li)
print(li)

# Method 2 using direct list property
li = [1,2,3,4,5,6,7,8,9]
li = li[::-1]
print(li)