# Sets are inmutable
s = {1, 3, "abc", "hello", 'a', 'c'}

# access all values in set
for x in s:
    print(x, end=' ')

# check for a value in set
if 3 in s :
    print(True)

# length of set
print(len(s))

# adding value to set
s.add('temp')
print(s)

# update values in set
b = {"new", "string"}
s.update(b)
print(s)

# delete value from set 
# remove returns error for not available
s.remove('a')
print(s)
# discard just do nothing for not available
s.discard("hello")
print(s)
# pop removes value from last
s.pop()
print(s)

# delete the whole set
del s