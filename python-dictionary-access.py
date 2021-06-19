dic = {'a':2 , 1:1 , 3:"hello" , "list":[1,2,3] , 'd':{'a':1 , 0:2}}

# finding values using keys
print(dic["list"])

# finding values using get(keys) -> default return none
print(dic.get('a'))
print(dic.get(5))

# return passed value if key not found
print(dic.get(5,"value"))

# get all the keys
print(dic.keys())

# get all the values
print(dic.values())

# get all the data pair 
print(dic.items())

# Iterating using for loop -> print keys
for i in dic :
    print(i)

# Iterating using for loop -> print values
for i in dic.values() :
    print(i)

