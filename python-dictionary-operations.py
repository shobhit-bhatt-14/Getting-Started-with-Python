dic = {1:2 , 'a':"hello" , 'l':[1, 2, 3]}

# Adding a new key : value pair
dic['str'] = 'Python'
print(dic)

# adding/updating key:value from another dictionary
d = {1:5 , 'c':5}
dic.update(d)
print(dic)

# remove a key:value pair
dic.pop('a')
print(dic)

# delete a key: value pair
del dic['c']
print(dic)

# clean all data inside dictionary
dic.clear()
print(dic)

# delete the complete dictionary
del dic