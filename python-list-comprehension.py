# Basically of the type list = [output traversal/loop conditions]

# new list with square of each element
li = [1, 2, 3, 4, 5]
l = [i**2 for i in li]
print(l)

# new list with square of only even element
li = [1, 2, 3, 4, 5]
l = [i**2 for i in li if i%2 == 0]
print(l)

# new list with square of only the element which are even and divisble by 3
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l = [i**2 for i in li if i%2 == 0 if i%3 == 0]
print(l)

# new list with common elements of two Lists
a = [1, 2, 3, 4, 5]
b = [1, 3, 5]
l = [i for i in a for j in b if i==j]
print(l)

# new list with square of only even element and rest same
li = [1, 2, 3, 4, 5]
l = [i**2 if i%2 == 0 else i for i in li]
print(l)

# new list with extracted characters from string
s = "Welcome to the world of Python !!"
l = [c for c in s if c != ' ']
print(l)

# new 2D List with extracted characters from an existing list of string
li = ["C", "Python", "Java", "C++", "Ruby", "JavaScript", "Julia", "R"]
l = [[p for p in i] for i in li]
print(l)