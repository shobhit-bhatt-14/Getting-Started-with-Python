# delete element using value in list
li = [1, 2.5, 'c', 'Python']
li.remove('c')
print(li)

# even if list has multiple values only the least index value is removed
li.append(1)
li.remove(1)
print(li)