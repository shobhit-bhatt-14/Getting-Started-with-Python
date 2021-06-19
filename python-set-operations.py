# none of these operations update the sets
a = {1, 2, 3, 4, 6, 8, 10}
b = {1, 2, 3, 5, 7, 9}

# Intersection of both the sets
print(a.intersection(b))

# Union of both the sets
print(a.union(b))

# difference between the sets
print(a.difference(b))
print(b.difference(a))

# uncommon between sets (or union-intersection)
print(a.symmetric_difference(b))

# Functions that update the sets
a = {1, 2, 3, 4, 6, 8, 10}
b = {1, 2, 3, 5, 7, 9}

# Intersection of both the sets updated to corresponding set
print(a.intersection_update(b))


# difference between the sets updated to corresponding set
print(a.difference_update(b))

# uncommon between sets (or union-intersection) updated to corresponding set
print(a.symmetric_difference_update(b))