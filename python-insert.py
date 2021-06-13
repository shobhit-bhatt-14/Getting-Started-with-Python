# insert(index,value) -> insert value at index in list
li = [1, 2.5, 'c', 'Python']
li.insert(3, 'hello')
print(li)

# insert(index,value) and len(list)<index => value added at the end
li.insert(10,545)
li.insert(4,[1, 2, 3])
print(li)