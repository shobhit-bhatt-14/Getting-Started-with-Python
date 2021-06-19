# Functions in sets
a = {1, 2, 3, 4, 6, 8}
b = {1, 2, 3, 5, 7, 9}
c = {1, 2, 3}
d = {5, 6, 7}

# check for subset
print(b.issubset(a))
print(c.issubset(a))

# check for superset
print(a.issuperset(b))
print(b.issuperset(c))

# check for disjoint
print(a.isdisjoint(b))
print(c.isdisjoint(d))