def fun(w, x=1, y=2, z=5) :
    return w+x+y+z

print(fun(10, 20, 30, 40))
print(fun(5, 10, 15))
print(fun(15, 20))

print(fun(8, 2, z=10))
print(fun(5, y=15))